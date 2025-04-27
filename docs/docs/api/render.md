---
title: render
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

```python
FLAG_MAPPING = {
    Constant: ATTR_FLAG,
    Function: FUNC_FLAG,
    Class: CLASS_FLAG,
    Module: MODULE_FLAG,
}
```

## 🅰 CUTTING\_MAPPING

```python
CUTTING_MAPPING = {
    "constant": -2,
    "function": -2,
    "class": -2,
    "method": -3,
    "module": -1,
} #+.!|")
```

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

```python
@contextmanager
def auto_fold(name: str, lines: list[str]):
```
## 🅵 get\_relative\_path

```python
def get_relative_path(dir_a, dir_b):
```
## 🅵 check\_type

```python
def check_type(obj):
```
## 🅵 format\_code

```python
def format_code(code: str, line_length: int = 80) -> str:
```
## 🅵 format\_signature

```python
def format_signature(signature: str) -> str:
```
## 🅵 handle\_name\_conflict

```python
def handle_name_conflict(fq_name: str, with_ext: bool = False) -> str:
```
## 🅵 try\_import\_module

```python
def try_import_module(module_name: str):
```
## 🅵 escaped\_markdown

```python
def escaped_markdown(text: str, simple=True) -> str:
```

## Classes

## 🅲 MarkdownRenderer

```python
class MarkdownRenderer:
    use_runtime = None
```


### 🅼 render

```python
def render(
    self,
    package: Package,
    output_path: Path | None = None,
    use_runtime: bool = True,
) -> None:
```

Render the given package as Markdown. If output\_path is None or '-', output to stdout.

If output\_path is a directory, each module gets its own file; otherwise, all modules go into one file.
### 🅼 \_render\_constant

```python
def _render_constant(self, const: Constant, indent=0) -> str:
```
### 🅼 render\_constant

```python
def render_constant(self, const: Constant, level: int = 2) -> list[str]:
```
### 🅼 render\_module

```python
def render_module(
    self, module: Module, level: int = 1, add_toc: bool = True
) -> list[str]:
```

Render a module section that includes the module's signature \(if any\), its docstring details,

and a table of contents linking to its classes, functions, constants, exports, and submodules.
### 🅼 \_try\_choose

```python
def _try_choose(self, value, alias, cur_level):
```
### 🅼 \_cross\_file\_link

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
### 🅼 render\_class\_toc

```python
def render_class_toc(
    self, module: Module, cls: Class, indent: int
) -> list[str]:
```

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

```python
def render_function(
    self, func: Function, level: int, flag=FUNC_FLAG, alias=None
) -> list[str]:
```

Render detailed documentation for a function/method including its signature and

docstring details \(parameters, returns, raises, etc.\).
### 🅼 \_try\_link

```python
def _try_link(
    self, text, cur_fq_name, runtime_module=None, cut_idx=0, alias=None
):
```
### 🅼 render\_docstring

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

Render detailed docstring information including description, parameters,

returns, raises, and attributes. An indent level can be provided for nested output.
### 🅼 link

```python
def link(self, module: Module, item: DocumentedItem | None = None) -> str:
```

Generate a link to a fully qualified name.
