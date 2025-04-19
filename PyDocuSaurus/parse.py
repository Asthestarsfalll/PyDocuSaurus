import ast
from .models import Module, Class, Function, Constant
from pathlib import Path
import docstring_parser
import astor
from docstring_parser.google import DEFAULT_SECTIONS
from .constants import DOCUSAURUS_SECTION

DEFAULT_SECTIONS.extend(list(DOCUSAURUS_SECTION.values()))


def should_include(name: str, include_private: bool) -> bool:
    """
    Returns True if the given name should be included based on the value
    of include_private. Always include dunder names like __init__.
    """
    if include_private:
        return True
    # Exclude names starting with a single underscore.
    if name.startswith("_") and not (name.startswith("__") and name.endswith("__")):
        return False
    return True


def get_string_value(node: ast.AST) -> str | None:
    """Extract a string from an AST node representing a constant."""
    if isinstance(node, ast.Constant) and isinstance(node.value, str):
        return node.value
    return None


def get_import_from(imported_name: str, module_ast: ast.Module):
    pass


def build_signature(node: ast.FunctionDef | ast.AsyncFunctionDef) -> str:
    """Construct a signature string for a function/method from its AST node."""
    args = node.args
    param_strings = []

    # Process positional arguments (with or without defaults)
    pos_args = args.args
    num_defaults = len(args.defaults)
    num_no_default = len(pos_args) - num_defaults
    for i, arg in enumerate(pos_args):
        param = arg.arg
        if arg.annotation:
            param += f": {ast.unparse(arg.annotation)}"
        if i >= num_no_default:
            default_val = args.defaults[i - num_no_default]
            param += f" = {ast.unparse(default_val)}"
        param_strings.append(param)

    # Process variable positional arguments (*args)
    if args.vararg:
        vararg = f"*{args.vararg.arg}"
        if args.vararg.annotation:
            vararg += f": {ast.unparse(args.vararg.annotation)}"
        param_strings.append(vararg)

    # Process keyword-only arguments
    for i, arg in enumerate(args.kwonlyargs):
        param = arg.arg
        if arg.annotation:
            param += f": {ast.unparse(arg.annotation)}"
        default = args.kw_defaults[i]
        if default is not None:
            param += f" = {ast.unparse(default)}"
        param_strings.append(param)

    # Process variable keyword arguments (**kwargs)
    if args.kwarg:
        kwarg = f"**{args.kwarg.arg}"
        if args.kwarg.annotation:
            kwarg += f": {ast.unparse(args.kwarg.annotation)}"
        param_strings.append(kwarg)

    params = ", ".join(param_strings)
    ret = ""
    if node.returns:
        ret = f" -> {ast.unparse(node.returns)}"
    return f"{node.name}({params}){ret}"


def parse_function(
    node: ast.FunctionDef | ast.AsyncFunctionDef,
    file_path: Path,
    parent: Class | Module,
) -> Function:
    """Parse a function or method node into a Function dataclass instance."""
    signature = build_signature(node)
    raw_doc = ast.get_docstring(node)
    parsed_doc = docstring_parser.parse(raw_doc) if raw_doc else None
    fq_name = f"{parent.fully_qualified_name}.{node.name}"
    return Function(
        path=file_path,
        name=node.name,
        fully_qualified_name=fq_name,
        signature=f"def {signature}:",
        docstring=parsed_doc,
    )


def parse_class(
    node: ast.ClassDef, parent: Module | Class, file_path: Path, include_private: bool
) -> Class:
    """Parse a class node into a Class dataclass instance and process its methods and nested classes."""
    raw_doc = ast.get_docstring(node)
    parsed_doc = docstring_parser.parse(raw_doc) if raw_doc else None
    fq_name = f"{parent.fully_qualified_name}.{node.name}"
    # Build a signature for the class, including base classes if any.
    if node.bases:
        bases = ", ".join(ast.unparse(base) for base in node.bases)
        signature = f"class {node.name}({bases}):"
    else:
        signature = f"class {node.name}:"
    cls = Class(
        path=file_path,
        name=node.name,
        fully_qualified_name=fq_name,
        signature=signature,
        docstring=parsed_doc,
        functions=[],
        classes=[],
    )
    # Process methods and nested classes.
    for child in node.body:
        if isinstance(child, (ast.FunctionDef, ast.AsyncFunctionDef)):
            if not should_include(child.name, include_private):
                continue
            method = parse_function(child, file_path, parent=cls)
            cls.functions.append(method)
        elif isinstance(child, ast.ClassDef):
            if not should_include(child.name, include_private):
                continue
            nested_cls = parse_class(
                child, parent=cls, file_path=file_path, include_private=include_private
            )
            cls.classes.append(nested_cls)
    return cls


def parse_module_docstring(module_ast: ast.Module) -> docstring_parser.Docstring | None:
    """Extract and parse the module docstring."""
    raw_doc = ast.get_docstring(module_ast)
    return docstring_parser.parse(raw_doc) if raw_doc else None


def parse_module_exports(module_ast: ast.Module) -> list[str]:
    """Extract __all__ exports from an __init__.py module if present."""
    exports: list = []
    for node in module_ast.body:
        if isinstance(node, ast.Assign):
            for target in node.targets:
                if isinstance(target, ast.Name) and target.id == "__all__":
                    if isinstance(node.value, (ast.List, ast.Tuple)):
                        for elt in node.value.elts:
                            value = get_string_value(elt)
                            if value:
                                #     import_from = get_import_from(value, module_ast)
                                # TODO
                                exports.append(value)
                    break
    return exports


def _get_comment_of_constants(code: str, line_number: int) -> str | None:
    lines = code.splitlines()
    comment = None
    target = min(line_number + 5, len(lines))
    while line_number < target:
        current_line = lines[line_number].strip()
        if "#" in current_line:
            comment = current_line.split("#")[-1].strip()
            break
        elif current_line.startswith('"""') or current_line.startswith("'''"):
            start_quote = current_line[:3]
            end_quote = current_line[-3:]
            if start_quote == end_quote:
                comment = current_line[3:-3]
                break
        line_number += 1
    return comment


def parse_module_constants(
    code: str,
    module_ast: ast.Module,
    module: Module,
    file_path: Path,
    include_private: bool,
) -> None:
    """Parse constants defined in a module.

    A constant is considered any assignment at module level whose target is a Name in ALL CAPS,
    excluding __all__. Supports both regular assignments (with optional type comments)
    and annotated assignments.
    """
    for node in module_ast.body:
        if isinstance(node, (ast.Assign, ast.AnnAssign)):
            # Process ast.Assign nodes (may have multiple targets).
            if isinstance(node, ast.Assign):
                for target in node.targets:
                    if (
                        isinstance(target, ast.Name)
                        and target.id.isupper()
                        and target.id != "__ALL__"
                        and should_include(target.id, include_private)
                    ):
                        type_annotation = None
                        if hasattr(node, "type_comment") and node.type_comment:
                            type_annotation = node.type_comment
                        # value = ast.unparse(node.value)
                        value = astor.to_source(node.value)
                        fq_name = f"{module.fully_qualified_name}.{target.id}"
                        constant = Constant(
                            path=file_path,
                            name=target.id,
                            fully_qualified_name=fq_name,
                            value=value,
                            type=type_annotation,
                            comment=_get_comment_of_constants(code, node.lineno),
                        )
                        module.constants.append(constant)
                        break
            # Process annotated assignments.
            elif isinstance(node, ast.AnnAssign):
                if (
                    isinstance(node.target, ast.Name)
                    and node.target.id.isupper()
                    and node.target.id != "__ALL__"
                    and should_include(node.target.id, include_private)
                ):
                    type_annotation = (
                        ast.unparse(node.annotation) if node.annotation else None
                    )
                    value = (
                        ast.unparse(node.value) if node.value is not None else "None"
                    )
                    fq_name = f"{module.fully_qualified_name}.{node.target.id}"
                    constant = Constant(
                        path=file_path,
                        name=node.target.id,
                        fully_qualified_name=fq_name,
                        value=value,
                        type=type_annotation,
                        comment=_get_comment_of_constants(code, node.lineno),
                    )
                    module.constants.append(constant)


def parse_module_functions(
    module_ast: ast.Module,
    module: Module,
    file_path: Path,
    include_private: bool,
) -> None:
    """Parse top-level functions in a module."""
    for node in module_ast.body:
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
            if not should_include(node.name, include_private):
                continue
            func = parse_function(node, file_path, parent=module)
            module.functions.append(func)


def parse_module_classes(
    module_ast: ast.Module,
    module: Module,
    file_path: Path,
    include_private: bool,
) -> None:
    """Parse classes in a module."""
    for node in module_ast.body:
        if isinstance(node, ast.ClassDef):
            if not should_include(node.name, include_private):
                continue
            cls = parse_class(
                node,
                parent=module,
                file_path=file_path,
                include_private=include_private,
            )
            module.classes.append(cls)


def parse_module_submodules(
    module: Module,
    file_path: Path,
    include_private: bool,
) -> None:
    """Parse submodules of a module."""
    for file_path in file_path.parent.iterdir():
        init_py = file_path / "__init__.py"
        if init_py.is_file():
            submodule = parse_module(
                init_py,
                f"{module.fully_qualified_name}.{file_path.name}",
                include_private,
            )
            module.submodules.append(submodule)
        elif file_path.suffix == ".py" and file_path.stem != "__init__":
            if (
                not include_private
                and file_path.name.startswith("_")
                and not file_path.name.startswith("__")
            ):
                continue
            submodule = parse_module(
                file_path,
                f"{module.fully_qualified_name}",
                include_private,
            )
            module.submodules.append(submodule)


def parse_module(
    file_path: Path,
    fully_qualified_name: str,
    include_private: bool,
) -> Module:
    """Parse a single module file into a Module dataclass instance."""
    with file_path.open("r", encoding="utf8") as f:
        source = f.read()
    module_ast = ast.parse(source, filename=str(file_path))
    mod_name = file_path.stem
    if mod_name != "__init__":
        fully_qualified_name = f"{fully_qualified_name}.{mod_name}"
    module = Module(
        path=file_path,
        name=mod_name,
        fully_qualified_name=fully_qualified_name,
        docstring=parse_module_docstring(module_ast),
        constants=[],
        functions=[],
        classes=[],
        exports=[],
    )
    parse_module_constants(source, module_ast, module, file_path, include_private)
    parse_module_functions(module_ast, module, file_path, include_private)
    parse_module_classes(module_ast, module, file_path, include_private)
    if mod_name == "__init__":
        module.exports = parse_module_exports(module_ast)
        parse_module_submodules(module, file_path, include_private)
    return module
