from __future__ import annotations
from contextlib import contextmanager

from .constants import (
    INDEX_TEMPLATE,
    MODULE_FLAG,
    CLASS_FLAG,
    FUNC_FLAG,
    ATTR_FLAG,
    DOCUSAURUS_SECTION,
    OBJECT_CACHE,
    FLAG_STR_MAPPING,
    UNKNOWN_FLAG,
    METHOD_FLAG,
    FLAG_EXPLAIN,
    COMMON_TYPE_LINKS,
    DETAIL_TEMPLATE_BEGINE,
    DETAIL_TEMPLATE_END,
    Return,
)
from . import constants
from functools import lru_cache, partial
import importlib
from .models import Package, Module, Constant, Class, Function, DocumentedItem
from pathlib import Path
import os
from collections import defaultdict
from black import Mode, format_str
import docstring_parser
import inspect

FLAG_MAPPING = {
    Constant: ATTR_FLAG,
    Function: FUNC_FLAG,
    Class: CLASS_FLAG,
    Module: MODULE_FLAG,
}

CUTTING_MAPPING = {
    "constant": -2,
    "function": -2,
    "class": -2,
    "method": -3,
    "module": -1,
}
_MARKDOWN_CHARACTERS_TO_ESCAPE = set(r"\`*_{}[]<>()#+.!|")
_MARKDOWN_CHARACTERS_TO_ESCAPE_SIMPLE = set(r"\`*__{}[]<>()#+!|")
USE_TYPE_FULL_NAME = False


@contextmanager
def auto_fold(name: str, lines: list[str]):
    idx = len(lines)
    yield
    count = 0
    for line in lines[idx:]:
        count += line.count("\n") or 1
        if count >= constants.MAX_LINES:
            lines.insert(idx, DETAIL_TEMPLATE_BEGINE.format(name))
            lines.append(DETAIL_TEMPLATE_END)
            break


def get_relative_path(dir_a, dir_b):
    dir_a = dir_a.rstrip(os.sep) + os.sep
    dir_b = dir_b.rstrip(os.sep) + os.sep

    parts_a = [p for p in dir_a.split(os.sep) if p]
    parts_b = [p for p in dir_b.split(os.sep) if p]

    common_length = 0
    for a, b in zip(parts_a, parts_b):
        if a == b:
            common_length += 1
        else:
            break

    up_levels = len(parts_a) - common_length

    relative_path = ("../" * up_levels) + "/".join(parts_b[common_length:])

    # if not relative_path.endswith('/'):
    #     relative_path += '/'

    return relative_path


def check_type(obj):
    if inspect.ismodule(obj):
        return "module"
    elif inspect.isclass(obj):
        return "class"
    elif inspect.ismethod(obj):
        return "method"
    elif inspect.isfunction(obj):
        return "function"
    else:
        return "constant"


def format_code(code: str, line_length: int = 80) -> str:
    mode = Mode(line_length=line_length)
    try:
        return format_str(code, mode=mode)
    except:  # noqa: E722
        print(f"Error while formatting code: {code}")
        return code


def format_signature(signature: str) -> str:
    full_code = f"{signature.strip()}\n    pass"
    formatted_code = format_code(full_code)
    return formatted_code.replace("pass", "").strip().strip("\n")


def handle_name_conflict(fq_name: str, with_ext: bool = False) -> str:
    split_names = fq_name.split(".")
    file_name = os.sep.join(fq_name.split(".")[1:])
    if len(split_names) > 2 and split_names[-1] == split_names[-2]:
        file_name = file_name + "_"
    if with_ext:
        file_name += ".md"
    file_name = file_name.replace("_", "-")
    return file_name.lower()


def try_import_module(module_name: str):
    try:
        return importlib.import_module(module_name)
    except ImportError as e:
        print("import error", e)
        return None


# fmt: off
# From https://stackoverflow.com/questions/68699165/how-to-escape-texts-for-formatting-in-python
def escaped_markdown(text: str, simple=True) -> str:
    if simple:
        return "".join(
            f"\\{character}"
            if character in _MARKDOWN_CHARACTERS_TO_ESCAPE_SIMPLE
            else character
            for character in text.strip()
        )
    return "".join(
        f"\\{character}" if character in _MARKDOWN_CHARACTERS_TO_ESCAPE else character
        for character in text.strip()
    )
# fmt: on


class MarkdownRenderer:
    use_runtime = None

    def render(
        self,
        package: Package,
        output_path: Path | None = None,
        use_runtime: bool = True,
    ) -> None:
        """
        Render the given package as Markdown. If output_path is None or '-', output to stdout.
        If output_path is a directory, each module gets its own file; otherwise, all modules go into one file.
        """
        self.use_runtime = use_runtime

        lines = [INDEX_TEMPLATE.format("API Reference")]
        lines.append(f"# `{package.name}`")
        lines.append("")
        lines.append(FLAG_EXPLAIN)
        lines.append("## Table of Contents")
        lines.append("")
        for module in package.modules:
            if "." not in module.fully_qualified_name:
                continue
            link = handle_name_conflict(module.fully_qualified_name)
            lines.append(
                f"- {MODULE_FLAG} [{escaped_markdown(module.fully_qualified_name)}](./{link})"
            )
        lines.append("")
        extra_lines = ""
        if output_path is not None:
            output_path.mkdir(parents=True, exist_ok=True)
            for module in package.modules:
                levels = module.fully_qualified_name.split(".")
                if len(levels) > 1:
                    relative_path = os.sep.join(levels[1:-1])
                file_name = self.link(module)
                module_lines = self.render_module(module, add_toc=len(levels) > 1)
                module_lines.append("")
                # module_output = INDEX_TEMPLATE.format(module.fully_qualified_name if module.name =='__init__' else file_name[:-3]) + "\n".join(module_lines)
                module_output = INDEX_TEMPLATE.format(file_name[:-3]) + "\n".join(
                    module_lines
                )
                file_name = handle_name_conflict(module.fully_qualified_name, True)
                if module.name == "__init__":
                    relative_path = os.sep.join(levels[1:])
                    if len(levels) > 1:
                        file_name = os.path.join(relative_path, "index.md")
                    else:
                        extra_lines = "\n".join(module_lines)
                        continue
                (output_path / relative_path).mkdir(parents=True, exist_ok=True)
                file_path = output_path / file_name
                file_path.write_text(module_output, encoding="utf8")
            # Write the index file table of contents linking to each module
            lines.append("")
            lines.append(extra_lines)
            (output_path / "index.md").write_text("\n".join(lines), encoding="utf8")

    def _render_constant(self, const: Constant, indent=0) -> str:
        value = const.value.strip("\n")
        type_str = f": {const.type}" if const.type else ""
        return "    " * indent + format_code(f"{const.name}{type_str} = {value}").strip(
            "\n"
        )

    def render_constant(self, const: Constant, level: int = 2) -> list[str]:
        lines: list[str] = []
        header_prefix = "#" * level
        lines.append(f"{header_prefix} {ATTR_FLAG} {escaped_markdown(const.name)}")
        lines.append("")
        with auto_fold(escaped_markdown(const.name), lines):
            lines.append("```python")
            lines.append(self._render_constant(const))
            if const.comment:
                lines[-1] += " #" + const.comment
            lines.append("```")
        return lines

    def render_module(
        self,
        module: Module,
        level: int = 1,
        add_toc: bool = True,
    ) -> list[str]:
        """
        Render a module section that includes the module's signature (if any), its docstring details,
        and a table of contents linking to its classes, functions, constants, exports, and submodules.
        """
        lines: list[str] = []
        header_prefix = "#" * level
        # Render module docstring details if available.
        if module.docstring:
            lines.extend(
                self.render_docstring(
                    module.docstring, module.fully_qualified_name, "module"
                )
            )
            lines.append("")
        if add_toc:
            lines.append(f"{header_prefix}# TOC")
        lines.append("")

        if module.exports and add_toc:
            # lines.append(f"- **[Exports](#{module.fully_qualified_name}-exports)**")
            lines.append("- **[Exports](#exports)**")
        # Second-level table of contents for this module.
        if module.constants:
            lines.append("- **Attributes:**")
            for const in module.constants:
                lines.append(
                    "  " * 1
                    + f"- {ATTR_FLAG} [{escaped_markdown(const.name, False)}]({self.link(module, const)})"
                    + (f" - {escaped_markdown(const.comment)}" if const.comment else "")
                )
        if module.functions:
            lines.append("- **Functions:**")
            for func in module.functions:
                lines.append(
                    "  " * 1
                    + f"- {FUNC_FLAG} [{escaped_markdown(func.name, False)}]({self.link(module, func)})"
                    + (
                        ""
                        if not func.docstring
                        else f" - {func.docstring.short_description}"
                    )
                )
        if module.classes:
            lines.append("- **Classes:**")
            for cls in module.classes:
                lines.extend(self.render_class_toc(module, cls, indent=1))
        if module.constants or module.functions or module.classes or module.exports:
            lines.append("")
        else:
            lines.clear()
            lines.append("## No Contents Are Generated")
            lines.append("")

        # Detailed sections.
        if module.constants:
            lines.append(f"{header_prefix}# Attributes")
            lines.append("")
            for const in module.constants:
                lines.extend(self.render_constant(const, level=level + 1))
                lines.append("")
            lines.append("")
        if module.functions:
            lines.append(f"{header_prefix}# Functions")
            lines.append("")
            for func in module.functions:
                lines.extend(self.render_function(func, level=level + 1))
            lines.append("")
        if module.classes:
            lines.append(f"{header_prefix}# Classes")
            lines.append("")
            for cls in module.classes:
                lines.extend(
                    self.render_class_details(
                        cls, level=level + 1, aliases=module.aliases
                    )
                )
            lines.append("")
        if module.exports:
            lines.append(f"{header_prefix}# Exports")
            lines.append("")
            runtime_module = (
                try_import_module(module.fully_qualified_name)
                if self.use_runtime
                else None
            )
            doc_base = module.fully_qualified_name.split(".")[0]
            for exp in module.exports:
                link, export_type, full_name = self._cross_file_link(
                    runtime_module,
                    module.fully_qualified_name,
                    exp,
                    doc_base,
                    alias=module.aliases.get(exp, None),
                )
                if link:
                    lines.append(
                        f"- {FLAG_STR_MAPPING[export_type]} [{escaped_markdown(full_name or exp)}]({link})"
                    )
                else:
                    lines.append(f"- {UNKNOWN_FLAG} {escaped_markdown(exp)}")
            lines.append("")
        lines.pop()
        return lines

    def _try_choose(self, value, alias, cur_level):
        def _get_info(v):
            info = OBJECT_CACHE.get(v, None)
            if info is None or len(info) == 1:
                return info
            target_key = cur_level + "." + value
            if target_key in info:
                return {target_key: info[target_key]}

        return _get_info(alias) or _get_info(value)

    @lru_cache(32)
    def _cross_file_link(
        self,
        runtime_module,
        cur_level,
        value,
        doc_base,
        cut_idx=0,
        need_type=False,
        alias=None,
    ):
        link = None
        full_name = None
        if info := self._try_choose(value, alias, cur_level):
            link = list(info.keys())[0]
            export_type = list(info.values())[0]
            if need_type and export_type in ["method", "function", "module"]:
                link = None
        elif (
            runtime_module
            and (runtime_exp := getattr(runtime_module, value, Return)) is not Return
        ):
            export_type = check_type(runtime_exp)
            if export_type == "module":
                link = runtime_exp.__name__
            else:
                link = runtime_exp.__module__
        else:
            export_type = None
        if export_type in ["class", "constant"]:
            link = link.replace("." + (alias or value), "", 1)
        flag = FLAG_STR_MAPPING.get(export_type, None)
        if flag:
            flag += "-"
        if link == cur_level:
            link = f"#{flag}{(alias or value).lower()}"
        elif link and link.split(".")[0] == doc_base:
            link = handle_name_conflict(link)
            if export_type == "method":
                link = os.sep.join(link.split(os.sep)[:-1])
            if cur_level := handle_name_conflict(cur_level):
                if cut_idx == 0:
                    link = get_relative_path(cur_level, link)
                else:
                    cur_level = os.path.join(*cur_level.split(os.sep)[:cut_idx])
                    link = get_relative_path(cur_level, link)
            if export_type != "module":
                link += f"#{flag}{(alias or value).lower()}"
        elif d := COMMON_TYPE_LINKS.get(value, None):
            link, full_name = d
            full_name = escaped_markdown(full_name)
        else:
            link = None
        return (
            link,
            export_type,
            full_name if USE_TYPE_FULL_NAME else value,
        )

    def render_class_toc(self, module: Module, cls: Class, indent: int) -> list[str]:
        """Render a TOC entry for a class and its nested classes."""
        lines: list[str] = []
        indent_str = "  " * indent
        lines.append(
            f"{indent_str}- {CLASS_FLAG} [{escaped_markdown(cls.name, False)}]({self.link(module, cls)})"
            + ("" if not cls.docstring else f" - {cls.docstring.short_description}")
        )
        for nested in cls.classes:
            lines.extend(self.render_class_toc(module, nested, indent + 1))
        return lines

    def render_class_details(self, cls: Class, level: int, aliases=None) -> list[str]:
        """
        Render detailed documentation for a class including its signature, docstring details,
        its methods, and any nested classes.
        """
        # runtime_module = try_import_module('.'.join(cls.fully_qualified_name.split('.')[:-1]))
        # runtime_cls = getattr(runtime_module, cls.name, Return)
        lines: list[str] = []
        header_prefix = "#" * level
        lines.append(f"{header_prefix} {CLASS_FLAG} {escaped_markdown(cls.name)}")
        lines.append("")
        with auto_fold(escaped_markdown(cls.name), lines):
            lines.append("```python")
            constants = [
                "\n" + self._render_constant(c, indent=1) for c in cls.constants
            ]
            lines.append(
                format_signature(
                    "".join([*cls.decorator_list, cls.signature, *constants])
                )
            )
            lines.append("```")
        lines.append("")
        if cls.docstring:
            lines.extend(
                self.render_docstring(
                    cls.docstring,
                    cls.fully_qualified_name,
                    "class",
                    alias=aliases.get(cls.name, None),
                )
            )
            lines.append("")
        if cls.functions:
            lines.append("")
            for func in cls.functions:
                lines.extend(
                    self.render_function(
                        func,
                        level=level + 1,
                        flag=METHOD_FLAG,
                        alias=aliases.get(func.name, None),
                    )
                )
            lines.append("")
        if cls.classes:
            # Flatten all nested classes in this class.
            for nested in cls.classes:
                lines.extend(self.render_class_details(nested, level=level))
            lines.append("")
        lines.pop()
        return lines

    def render_function(
        self, func: Function, level: int, flag=FUNC_FLAG, alias=None
    ) -> list[str]:
        """
        Render detailed documentation for a function/method including its signature and
        docstring details (parameters, returns, raises, etc.).
        """
        lines: list[str] = []
        header_prefix = "#" * level
        lines.append(f"{header_prefix} {flag} {escaped_markdown(func.name, False)}")
        lines.append("")
        with auto_fold(escaped_markdown(func.name), lines):
            lines.append("```python")
            lines.append(
                format_signature("".join([*func.decorator_list, func.signature]))
            )
            lines.append("```")
        lines.append("")
        if func.docstring:
            lines.extend(
                self.render_docstring(
                    func.docstring,
                    func.fully_qualified_name,
                    "function" if flag == FUNC_FLAG else "method",
                    alias=alias,
                )
            )
            lines.append("")
        lines.pop()
        return lines

    def _try_link(self, text, cur_fq_name, runtime_module=None, cut_idx=0, alias=None):
        split_text = text.split(" | ")

        def _inner(t):
            t = t.strip()
            link, _, full_name = self._cross_file_link(
                runtime_module=runtime_module,
                cur_level=cur_fq_name,
                value=t.strip(),
                doc_base=cur_fq_name.split(".")[0],
                cut_idx=cut_idx,
                need_type=True,
                alias=alias,
            )
            if not link:
                return t
            return f"[{full_name or t}]({link})"

        return " | ".join([_inner(x) for x in split_text])

    def render_docstring(
        self,
        doc: docstring_parser.Docstring,
        parent_fq_name: str,
        parent_type: int,
        indent: int = 0,
        simple=True,
        alias=None,
    ) -> list[str]:
        """
        Render detailed docstring information including description, parameters,
        returns, raises, and attributes. An indent level can be provided for nested output.
        """
        cut_idx = CUTTING_MAPPING[parent_type]
        _try = partial(
            self._try_link, cut_idx=cut_idx, cur_fq_name=parent_fq_name, alias=alias
        )
        indent_str = "  " * indent
        lines: list[str] = []
        if doc.short_description:
            lines.append(
                f"{indent_str}{escaped_markdown(doc.short_description, simple)}"
            )
            lines.append("")
        if doc.long_description:
            lines.append(
                f"{indent_str}{escaped_markdown(doc.long_description, simple)}"
            )
            lines.append("")
        if doc.params:
            lines.append(f"{indent_str}**Parameters:**")
            lines.append("")
            for param in doc.params:
                line = f"{indent_str}- **{param.arg_name}**"
                if param.type_name:
                    line += f" ({_try(param.type_name)})"
                if param.default:
                    line += f" (default to `{param.default}`)"
                if param.description:
                    line += f": {escaped_markdown(param.description, simple)}"
                lines.append(line)
            lines.append("")
        if doc.attrs:
            lines.append(f"{indent_str}**Attributes:**")
            lines.append("")
            for attr in doc.attrs:
                line = f"{indent_str}- **{attr.arg_name}**"
                if attr.type_name:
                    line += f" ({_try(attr.type_name)})"
                if attr.description:
                    line += f": {escaped_markdown(attr.description, simple)}"
                lines.append(line)
            lines.append("")
        if doc.returns:
            lines.append(f"{indent_str}**Returns:**")
            lines.append("")
            ret_line = ""
            if doc.returns.type_name:
                ret_line += f"**{_try(doc.returns.type_name)}**: "
            if doc.returns.description:
                ret_line += f"{escaped_markdown(doc.returns.description, simple)}"
            else:
                # Trim the trailing colon if no description is provided.
                ret_line = ret_line[:-2]
            lines.append(f"{indent_str}- {ret_line}")
            lines.append("")
        if doc.raises:
            lines.append(f"{indent_str}**Raises:**")
            lines.append("")
            for raise_item in doc.raises:
                raise_line = f"{indent_str}- **{_try(raise_item.type_name) or ''}**: "
                if raise_item.description:
                    raise_line += f"{escaped_markdown(raise_item.description, simple)}"
                else:
                    raise_line = raise_line[:-2]
                lines.append(raise_line)
            lines.append("")
        if doc.examples:
            lines.append(f"{indent_str}**Examples:**")
            lines.append("")
            for example in doc.examples:
                lines.append("```python")
                lines.append(f"{example.description}")
                lines.append("```")
            lines.append("")
        doucsaurus_section = defaultdict(list)
        for section_name in DOCUSAURUS_SECTION:
            for item in doc.meta:
                if section_name in item.args:
                    doucsaurus_section[section_name].append(item.description)
        for section_name, description in doucsaurus_section.items():
            lines.append(f"{indent_str}:::{section_name}")
            for desc in description:
                lines.append(f"{desc}")
                lines.append("")
            lines.append(f"{indent_str}:::")
            lines.append("")
        lines.pop()
        return lines

    def link(
        self,
        module: Module,
        item: DocumentedItem | None = None,
    ) -> str:
        """
        Generate a link to a fully qualified name.
        """
        if item is None:
            return f"{module.fully_qualified_name.split('.')[-1]}.md"
        else:
            return f"#{FLAG_MAPPING[item.__class__]}-{item.fully_qualified_name.split('.')[-1].lower()}"
