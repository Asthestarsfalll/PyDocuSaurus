from __future__ import annotations

from .constants import (
    INDEX_TEMPLATE,
    MODULE_FLAG,
    CLASS_FLAG,
    FUNC_FLAG,
    ATTR_FLAG,
    DOCUSAURUS_SECTION,
)
from .models import Package, Module, Constant, Class, Function, DocumentedItem
from pathlib import Path
import os
from collections import defaultdict
from black import Mode, format_str
import docstring_parser

FLAG_MAPPING = {
    Constant: ATTR_FLAG,
    Function: FUNC_FLAG,
    Class: CLASS_FLAG,
    Module: MODULE_FLAG,
}
_MARKDOWN_CHARACTERS_TO_ESCAPE = set(r"\`*_{}[]<>()#+.!|")
_MARKDOWN_CHARACTERS_TO_ESCAPE_SIMPLE = set(r"\`*__{}[]<>()#+!|")


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


def handle_name_conflict(file_name: str, fq_name: str, with_ext: bool = False) -> str:
    if "." in file_name:
        file_name = ".".join(file_name.split(".")[:-1])
    file_name = file_name.replace("-", "_")
    if "." in fq_name and file_name.split(os.sep)[-1] == fq_name.split(".")[-2]:
        file_name = file_name + "_"
    if with_ext:
        file_name += ".md"
    file_name = file_name.replace("_", "-")
    return file_name


def colorize(docstring: str, color="red") -> str:
    return f"[{docstring}](#{docstring.replace(' ', '')})"


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
    def render(self, package: Package, output_path: Path | None = None) -> None:
        """
        Render the given package as Markdown. If output_path is None or '-', output to stdout.
        If output_path is a directory, each module gets its own file; otherwise, all modules go into one file.
        """
        lines = [INDEX_TEMPLATE.format("API Reference")]
        lines.append(f"# `{package.name}`")
        lines.append("")
        lines.append("## Table of Contents")
        lines.append("")
        for module in package.modules:
            if "." not in module.fully_qualified_name:
                continue
            link = f"{os.sep.join(module.fully_qualified_name.split('.')[1:]).replace('_', '-')}"
            link = handle_name_conflict(link, module.fully_qualified_name)
            lines.append(
                f"- {MODULE_FLAG} [{escaped_markdown(module.fully_qualified_name)}](./{link})"
            )
        lines.append("")
        extra_lines = ""
        if output_path is not None:
            output_path.mkdir(parents=True, exist_ok=True)
            for module in package.modules:
                levels = module.fully_qualified_name.split(".")
                relative_path = ""
                if len(levels) > 1:
                    relative_path = os.sep.join(levels[1:-1])
                file_name = self.link(module)
                module_lines = self.render_module(module, add_toc=len(levels) > 1)
                module_lines.append("")
                # module_output = INDEX_TEMPLATE.format(module.fully_qualified_name if module.name =='__init__' else file_name[:-3]) + "\n".join(module_lines)
                module_output = INDEX_TEMPLATE.format(file_name[:-3]) + "\n".join(
                    module_lines
                )
                if module.name == "__init__":
                    relative_path = os.sep.join(levels[1:])
                    if len(levels) > 1:
                        file_name = "index.md"
                    else:
                        extra_lines = "\n".join(module_lines)
                        continue
                (output_path / relative_path).mkdir(parents=True, exist_ok=True)
                file_name = handle_name_conflict(
                    file_name, module.fully_qualified_name, True
                )
                file_path = output_path / relative_path / file_name
                file_path.write_text(module_output, encoding="utf8")
            # Write the index file table of contents linking to each module
            lines.append("")
            lines.append(extra_lines)
            (output_path / "index.md").write_text("\n".join(lines), encoding="utf8")

    def render_constant(self, const: Constant, level: int = 2) -> list[str]:
        lines: list[str] = []
        header_prefix = "#" * level
        type_str = f": {const.type}" if const.type else ""
        lines.append(f"{header_prefix} {ATTR_FLAG} {escaped_markdown(const.name)}")
        lines.append("")
        lines.append("```python")
        value = const.value.strip("\n")
        lines.append(format_code(f"{const.name}{type_str} = {value}").strip("\n"))
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
        if add_toc:
            lines.append(f"{header_prefix}# TOC")
        lines.append("")

        # Render module docstring details if available.
        if module.docstring:
            lines.extend(self.render_docstring(module.docstring))
            lines.append("")
        if module.exports and add_toc:
            lines.append(f"- **[Exports](#{module.fully_qualified_name}-exports)**")
        # Second-level table of contents for this module.
        if module.constants:
            lines.append("- **Attributes:**")
            for const in module.constants:
                lines.append(
                    "  " * 1
                    + f"- {ATTR_FLAG} [{escaped_markdown(const.name, False)}]({self.link(module, const)})"
                    + f" - {const.comment}"
                    if const.comment
                    else ""
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

        # Detailed sections.
        if module.constants:
            lines.append(f"{header_prefix}# Attributes")
            lines.append("")
            for const in module.constants:
                lines.extend(self.render_constant(const, level=level + 1))
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
                lines.extend(self.render_class_details(cls, level=level + 1))
            lines.append("")
        if module.exports:
            lines.append(f"{header_prefix}# Exports")
            lines.append("")
            for exp in module.exports:
                link = os.sep.join(module.fully_qualified_name.split(".")[-1:])
                # link = handle_name_conflict(link, module.fully_qualified_name)
                lines.append(f"- {MODULE_FLAG} [{escaped_markdown(exp)}](./{link})")
            lines.append("")
        lines.pop()
        return lines

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

    def render_class_details(self, cls: Class, level: int) -> list[str]:
        """
        Render detailed documentation for a class including its signature, docstring details,
        its methods, and any nested classes.
        """
        lines: list[str] = []
        header_prefix = "#" * level
        lines.append(f"{header_prefix} {CLASS_FLAG} {escaped_markdown(cls.name)}")
        lines.append("")
        lines.append("```python")
        lines.append(cls.signature)
        lines.append("```")
        lines.append("")
        if cls.docstring:
            lines.extend(self.render_docstring(cls.docstring))
            lines.append("")
        if cls.functions:
            lines.append("**Functions:**")
            lines.append("")
            for func in cls.functions:
                lines.extend(self.render_function(func, level=level + 1))
            lines.append("")
        if cls.classes:
            # Flatten all nested classes in this class.
            for nested in cls.classes:
                lines.extend(self.render_class_details(nested, level=level))
            lines.append("")
        lines.pop()
        return lines

    def render_function(self, func: Function, level: int) -> list[str]:
        """
        Render detailed documentation for a function/method including its signature and
        docstring details (parameters, returns, raises, etc.).
        """
        lines: list[str] = []
        header_prefix = "#" * level
        lines.append(
            f"{header_prefix} {FUNC_FLAG} {escaped_markdown(func.name, False)}"
        )
        lines.append("")
        lines.append("```python")
        lines.append(format_signature(func.signature))
        lines.append("```")
        lines.append("")
        if func.docstring:
            lines.extend(self.render_docstring(func.docstring))
            lines.append("")
        lines.pop()
        return lines

    def render_docstring(
        self,
        doc: docstring_parser.Docstring,
        indent: int = 0,
        simple=True,
    ) -> list[str]:
        """
        Render detailed docstring information including description, parameters,
        returns, raises, and attributes. An indent level can be provided for nested output.
        """
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
                line = f"{indent_str}- **{colorize(param.arg_name)}**"
                if param.type_name:
                    line += f" ({param.type_name})"
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
                line = f"{indent_str}- **{colorize(attr.arg_name)}**"
                if attr.type_name:
                    line += f" ({attr.type_name})"
                if attr.description:
                    line += f": {escaped_markdown(attr.description, simple)}"
                lines.append(line)
            lines.append("")
        if doc.returns:
            lines.append(f"{indent_str}**Returns:**")
            lines.append("")
            ret_line = ""
            if doc.returns.type_name:
                ret_line += f"**{colorize(doc.returns.type_name)}**: "
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
                raise_line = (
                    f"{indent_str}- **{colorize(raise_item.type_name or '')}**: "
                )
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
