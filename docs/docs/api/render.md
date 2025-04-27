---
title: render
sidebar_position: 3
---

## TOC

- **Attributes:**
  - 🅰 [FLAG\_MAPPING](#🅰-flag_mapping)
  - 🅰 [CUTTING\_MAPPING](#🅰-cutting_mapping) - \+.\!\|"\)
  - 🅰 [\_MARKDOWN\_CHARACTERS\_TO\_ESCAPE](#🅰-_markdown_characters_to_escape) - \+.\!\|"\)
  - 🅰 [\_MARKDOWN\_CHARACTERS\_TO\_ESCAPE\_SIMPLE](#🅰-_markdown_characters_to_escape_simple) - \+\!\|"\)
  - 🅰 [USE\_TYPE\_FULL\_NAME](#🅰-use_type_full_name)
- **Functions:**
  - 🅵 [auto\_fold](#🅵-auto_fold)
  - 🅵 [get\_relative\_path](#🅵-get_relative_path)
  - 🅵 [check\_type](#🅵-check_type)
  - 🅵 [format\_code](#🅵-format_code)
  - 🅵 [format\_signature](#🅵-format_signature)
  - 🅵 [handle\_name\_conflict](#🅵-handle_name_conflict)
  - 🅵 [try\_import\_module](#🅵-try_import_module)
  - 🅵 [escaped\_markdown](#🅵-escaped_markdown)
- **Classes:**
  - 🅲 [MarkdownRenderer](#🅲-markdownrenderer)

## Attributes

## 🅰 FLAG\_MAPPING

<details>

<summary>FLAG\_MAPPING</summary>
```python
FLAG_MAPPING = {
    Constant: ATTR_FLAG,
    Function: FUNC_FLAG,
    Class: CLASS_FLAG,
    Module: MODULE_FLAG,
}
```

</details>


## 🅰 CUTTING\_MAPPING

<details>

<summary>CUTTING\_MAPPING</summary>
```python
CUTTING_MAPPING = {
    "constant": -2,
    "function": -2,
    "class": -2,
    "method": -3,
    "module": -1,
} #+.!|")
```

</details>


## 🅰 \_MARKDOWN\_CHARACTERS\_TO\_ESCAPE

```python
_MARKDOWN_CHARACTERS_TO_ESCAPE = set("\\`*_{}[]<>()#+.!|") #+.!|")
```

## 🅰 \_MARKDOWN\_CHARACTERS\_TO\_ESCAPE\_SIMPLE

```python
_MARKDOWN_CHARACTERS_TO_ESCAPE_SIMPLE = set("\\`*__{}[]<>()#+!|") #+!|")
```

## 🅰 USE\_TYPE\_FULL\_NAME

```python
USE_TYPE_FULL_NAME = False
```


## Functions

## 🅵 auto\_fold

<details>

<summary>auto\_fold</summary>
```python
@contextmanager
def auto_fold(name: str, lines: list[str]):
    idx = len(lines)
    yield
    count = 0
    for line in lines[idx:]:
        count += line.count("\n") or 0
        if count >= constants.MAX_LINES:
            lines.insert(idx, DETAIL_TEMPLATE_BEGINE.format(name))
            lines.append(DETAIL_TEMPLATE_END)
            break
```

</details>

## 🅵 get\_relative\_path

<details>

<summary>get\_relative\_path</summary>
```python
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
    relative_path = "../" * up_levels + "/".join(parts_b[common_length:])
    return relative_path
```

</details>

## 🅵 check\_type

<details>

<summary>check\_type</summary>
```python
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
```

</details>

## 🅵 format\_code

<details>

<summary>format\_code</summary>
```python
def format_code(code: str, line_length: int = 80) -> str:
    mode = Mode(line_length=line_length)
    try:
        return format_str(code, mode=mode)
    except:
        print(f"Error while formatting code: {code}")
        return code
```

</details>

## 🅵 format\_signature

```python
def format_signature(signature: str) -> str:
    full_code = f"""{signature.strip()}
    """
    formatted_code = format_code(full_code)
    return formatted_code.replace("", "").strip().strip("\n")
```
## 🅵 handle\_name\_conflict

<details>

<summary>handle\_name\_conflict</summary>
```python
def handle_name_conflict(fq_name: str, with_ext: bool = False) -> str:
    split_names = fq_name.split(".")
    file_name = os.sep.join(fq_name.split(".")[1:])
    if len(split_names) > 2 and split_names[-1] == split_names[-2]:
        file_name = file_name + "_"
    if with_ext:
        file_name += ".md"
    file_name = file_name.replace("_", "-")
    return file_name.lower()
```

</details>

## 🅵 try\_import\_module

<details>

<summary>try\_import\_module</summary>
```python
def try_import_module(module_name: str):
    try:
        return importlib.import_module(module_name)
    except ImportError as e:
        print("import error", e)
        return None
```

</details>

## 🅵 escaped\_markdown

<details>

<summary>escaped\_markdown</summary>
```python
def escaped_markdown(text: str, simple=True) -> str:
    if simple:
        return "".join(
            (
                f"\\{character}"
                if character in _MARKDOWN_CHARACTERS_TO_ESCAPE_SIMPLE
                else character
            )
            for character in text.strip()
        )
    return "".join(
        (
            f"\\{character}"
            if character in _MARKDOWN_CHARACTERS_TO_ESCAPE
            else character
        )
        for character in text.strip()
    )
```

</details>


## Classes

## 🅲 MarkdownRenderer

```python
class MarkdownRenderer:
    use_runtime = None
```


### 🅼 render

<details>

<summary>render</summary>
```python
def render(
    self,
    package: Package,
    output_path: Path | None = None,
    use_runtime: bool = True,
) -> None:
```

</details>


Render the given package as Markdown. If output\_path is None or '-', output to stdout.

If output\_path is a directory, each module gets its own file; otherwise, all modules go into one file.
### 🅼 \_render\_constant

<details>

<summary>\_render\_constant</summary>
```python
def _render_constant(self, const: Constant, indent=0) -> str:
    value = const.value.strip("\n")
    type_str = f": {const.type}" if const.type else ""
    return "    " * indent + format_code(
        f"{const.name}{type_str} = {value}"
    ).strip("\n")
```

</details>

### 🅼 render\_constant

<details>

<summary>render\_constant</summary>
```python
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
```

</details>

### 🅼 render\_module

```python
def render_module(
    self, module: Module, level: int = 1, add_toc: bool = True
) -> list[str]:
```

Render a module section that includes the module's signature \(if any\), its docstring details,

and a table of contents linking to its classes, functions, constants, exports, and submodules.
### 🅼 \_try\_choose

<details>

<summary>\_try\_choose</summary>
```python
def _try_choose(self, value, alias, cur_level):

    def _get_info(v):
        info = OBJECT_CACHE.get(v, None)
        if info is None or len(info) == 1:
            return info
        target_key = cur_level + "." + value
        if target_key in info:
            return {target_key: info[target_key]}

    return _get_info(alias) or _get_info(value)
```

</details>

### 🅼 \_cross\_file\_link

<details>

<summary>\_cross\_file\_link</summary>
```python
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
```

</details>

### 🅼 render\_class\_toc

<details>

<summary>render\_class\_toc</summary>
```python
def render_class_toc(
    self, module: Module, cls: Class, indent: int
) -> list[str]:
    lines: list[str] = []
    indent_str = "  " * indent
    lines.append(
        f"{indent_str}- {CLASS_FLAG} [{escaped_markdown(cls.name, False)}]({self.link(module, cls)})"
        + ("" if not cls.docstring else f" - {cls.docstring.short_description}")
    )
    for nested in cls.classes:
        lines.extend(self.render_class_toc(module, nested, indent + 1))
    return lines
```

</details>


Render a TOC entry for a class and its nested classes.
### 🅼 render\_class\_details

```python
def render_class_details(
    self, cls: Class, level: int, aliases=None
) -> list[str]:
```

Render detailed documentation for a class including its signature, docstring details,

its methods, and any nested classes.
### 🅼 render\_function

<details>

<summary>render\_function</summary>
```python
def render_function(
    self, func: Function, level: int, flag=FUNC_FLAG, alias=None
) -> list[str]:
    lines: list[str] = []
    header_prefix = "#" * level
    lines.append(f"{header_prefix} {flag} {escaped_markdown(func.name, False)}")
    lines.append("")
    with auto_fold(escaped_markdown(func.name), lines):
        lines.append("```python")
        lines.append(
            format_signature(
                func.body or "".join([*func.decorator_list, func.signature])
            )
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
```

</details>


Render detailed documentation for a function/method including its signature and

docstring details \(parameters, returns, raises, etc.\).
### 🅼 \_try\_link

```python
def _try_link(
    self, text, cur_fq_name, runtime_module=None, cut_idx=0, alias=None
):
```
### 🅼 render\_docstring

<details>

<summary>render\_docstring</summary>
```python
def render_docstring(
    self,
    doc: docstring_parser.Docstring,
    parent_fq_name: str,
    parent_type: int,
    indent: int = 0,
    simple=True,
    alias=None,
) -> list[str]:
```

</details>


Render detailed docstring information including description, parameters,

returns, raises, and attributes. An indent level can be provided for nested output.
### 🅼 link

```python
def link(self, module: Module, item: DocumentedItem | None = None) -> str:
    if item is None:
        return f"{module.fully_qualified_name.split('.')[-1]}.md"
    else:
        return f"#{FLAG_MAPPING[item.__class__]}-{item.fully_qualified_name.split('.')[-1].lower()}"
```

Generate a link to a fully qualified name.
