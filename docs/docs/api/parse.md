---
title: parse
sidebar_position: 3
---

## TOC

- **Functions:**
  - 🅵 [should\_include](#🅵-should_include) - Returns True if the given name should be included based on the value
  - 🅵 [get\_string\_value](#🅵-get_string_value) - Extract a string from an AST node representing a constant.
  - 🅵 [build\_signature](#🅵-build_signature) - Construct a signature string for a function/method from its AST node.
  - 🅵 [parse\_function](#🅵-parse_function) - Parse a function or method node into a Function dataclass instance.
  - 🅵 [parse\_class](#🅵-parse_class) - Parse a class node into a Class dataclass instance and process its methods and nested classes.
  - 🅵 [parse\_module\_docstring](#🅵-parse_module_docstring) - Extract and parse the module docstring.
  - 🅵 [parse\_module\_exports](#🅵-parse_module_exports) - Extract __all__ exports from an __init__.py module if present and parse import aliases.
  - 🅵 [\_get\_comment\_of\_constants](#🅵-_get_comment_of_constants)
  - 🅵 [parse\_constants](#🅵-parse_constants)
  - 🅵 [parse\_module\_constants](#🅵-parse_module_constants) - Parse constants defined in a module.
  - 🅵 [parse\_module\_functions](#🅵-parse_module_functions) - Parse top-level functions in a module.
  - 🅵 [parse\_module\_classes](#🅵-parse_module_classes) - Parse classes in a module.
  - 🅵 [parse\_module\_submodules](#🅵-parse_module_submodules) - Parse submodules of a module.
  - 🅵 [parse\_module](#🅵-parse_module) - Parse a single module file into a Module dataclass instance.

## Functions

## 🅵 should\_include

<details>

<summary>should\_include</summary>
```python
def should_include(name: str, include_private: bool) -> bool:
    if include_private:
        return True
    if name.startswith("_") and not (
        name.startswith("__") and name.endswith("__")
    ):
        return False
    return True
```

</details>


Returns True if the given name should be included based on the value

of include\_private. Always include dunder names like \_\_init\_\_.
## 🅵 get\_string\_value

```python
def get_string_value(node: ast.AST) -> str | None:
    if isinstance(node, ast.Constant) and isinstance(node.value, str):
        return node.value
    return None
```

Extract a string from an AST node representing a constant.
## 🅵 build\_signature

```python
def build_signature(node: ast.FunctionDef | ast.AsyncFunctionDef) -> str:
```

Construct a signature string for a function/method from its AST node.
## 🅵 parse\_function

<details>

<summary>parse\_function</summary>
```python
def parse_function(
    node: ast.FunctionDef | ast.AsyncFunctionDef,
    file_path: Path,
    parent: Class | Module,
    type: str = "function",
) -> Function:
    signature = build_signature(node)
    raw_doc = ast.get_docstring(node)
    parsed_doc = docstring_parser.parse(raw_doc) if raw_doc else None
    fq_name = f"{parent.fully_qualified_name}.{node.name}"
    OBJECT_CACHE[node.name][parent.fully_qualified_name] = type
    code = astor.to_source(node)
    return Function(
        path=file_path,
        name=node.name,
        fully_qualified_name=fq_name,
        signature=f"def {signature}:",
        docstring=parsed_doc,
        decorator_list=[
            ("@" + astor.to_source(d)) for d in node.decorator_list
        ],
        body=code if code.count("\n") < constants.INCLUDE_LINES else None,
    )
```

</details>


Parse a function or method node into a Function dataclass instance.
## 🅵 parse\_class

<details>

<summary>parse\_class</summary>
```python
def parse_class(
    node: ast.ClassDef,
    parent: Module | Class,
    file_path: Path,
    include_private: bool,
    code: str,
) -> Class:
```

</details>


Parse a class node into a Class dataclass instance and process its methods and nested classes.
## 🅵 parse\_module\_docstring

```python
def parse_module_docstring(
    module_ast: ast.Module,
) -> docstring_parser.Docstring | None:
    raw_doc = ast.get_docstring(module_ast)
    return docstring_parser.parse(raw_doc) if raw_doc else None
```

Extract and parse the module docstring.
## 🅵 parse\_module\_exports

<details>

<summary>parse\_module\_exports</summary>
```python
def parse_module_exports(
    module_ast: ast.Module,
) -> tuple[list[str], dict[str, str]]:
    exports: list[str] = []
    aliases: dict[str, str] = {}
    for node in module_ast.body:
        if isinstance(node, ast.Assign):
            for target in node.targets:
                if isinstance(target, ast.Name) and target.id == "__all__":
                    if isinstance(node.value, (ast.List, ast.Tuple)):
                        for elt in node.value.elts:
                            value = get_string_value(elt)
                            if value:
                                exports.append(value)
                    break
        elif isinstance(node, (ast.Import, ast.ImportFrom)):
            for alias in node.names:
                if alias.asname:
                    aliases[alias.asname] = alias.name
    return exports, aliases
```

</details>


Extract \_\_all\_\_ exports from an \_\_init\_\_.py module if present and parse import aliases.

**Returns:**

- **[tuple](https://docs.python.org/3/library/stdtypes.html#tuples)**: A tuple containing:
- list of exported names from \_\_all\_\_
- dictionary mapping original names to their aliases \(from 'import as'\)
## 🅵 \_get\_comment\_of\_constants

<details>

<summary>\_get\_comment\_of\_constants</summary>
```python
def _get_comment_of_constants(code: str, line_number: int) -> str | None:
    lines = code.splitlines()
    comment = None
    target = min(line_number + 10, len(lines))
    line_number -= 1
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
```

</details>

## 🅵 parse\_constants

```python
def parse_constants(node, code, module, file_path, include_private, cache=True):
```
## 🅵 parse\_module\_constants

<details>

<summary>parse\_module\_constants</summary>
```python
def parse_module_constants(
    code: str,
    module_ast: ast.Module,
    module: Module,
    file_path: Path,
    include_private: bool,
) -> None:
    for node in module_ast.body:
        if isinstance(node, ast.If) and constants.INCLUDE_IF:
            for subnode in node.body:
                parse_constants(
                    subnode, code, module, file_path, include_private
                )
        parse_constants(node, code, module, file_path, include_private)
```

</details>


Parse constants defined in a module.

A constant is considered any assignment at module level whose target is a Name in ALL CAPS,
excluding \_\_all\_\_. Supports both regular assignments \(with optional type comments\)
and annotated assignments.
## 🅵 parse\_module\_functions

<details>

<summary>parse\_module\_functions</summary>
```python
def parse_module_functions(
    module_ast: ast.Module,
    module: Module,
    file_path: Path,
    include_private: bool,
) -> None:
    for node in module_ast.body:
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
            if not should_include(node.name, include_private):
                continue
            func = parse_function(node, file_path, parent=module)
            module.functions.append(func)
        elif isinstance(node, ast.If) and constants.INCLUDE_IF:
            parse_module_functions(node, module, file_path, include_private)
```

</details>


Parse top-level functions in a module.
## 🅵 parse\_module\_classes

<details>

<summary>parse\_module\_classes</summary>
```python
def parse_module_classes(
    code: str,
    module_ast: ast.Module,
    module: Module,
    file_path: Path,
    include_private: bool,
) -> None:
    for node in module_ast.body:
        if isinstance(node, ast.ClassDef):
            if not should_include(node.name, include_private):
                continue
            cls = parse_class(
                node,
                parent=module,
                file_path=file_path,
                include_private=include_private,
                code=code,
            )
            module.classes.append(cls)
        elif isinstance(node, ast.If) and constants.INCLUDE_IF:
            parse_module_classes(code, node, module, file_path, include_private)
```

</details>


Parse classes in a module.
## 🅵 parse\_module\_submodules

<details>

<summary>parse\_module\_submodules</summary>
```python
def parse_module_submodules(
    module: Module, file_path: Path, include_private: bool
) -> None:
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
                file_path, f"{module.fully_qualified_name}", include_private
            )
            module.submodules.append(submodule)
```

</details>


Parse submodules of a module.
## 🅵 parse\_module

<details>

<summary>parse\_module</summary>
```python
def parse_module(
    file_path: Path, fully_qualified_name: str, include_private: bool
) -> Module:
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
        aliases={},
    )
    parse_module_constants(
        source, module_ast, module, file_path, include_private
    )
    parse_module_functions(module_ast, module, file_path, include_private)
    parse_module_classes(source, module_ast, module, file_path, include_private)
    if mod_name == "__init__":
        module.exports, module.aliases = parse_module_exports(module_ast)
        parse_module_submodules(module, file_path, include_private)
    return module
```

</details>


Parse a single module file into a Module dataclass instance.
