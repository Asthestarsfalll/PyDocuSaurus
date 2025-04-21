---
title: render
---

## TOC

- **Attributes:**
  - 🅰 [FLAG\_MAPPING](#🅰-flag_mapping) - \+.\!\|"\)
- **Functions:**
  - 🅵 [check\_type](#🅵-check_type)
  - 🅵 [format\_code](#🅵-format_code)
  - 🅵 [format\_signature](#🅵-format_signature)
  - 🅵 [handle\_name\_conflict](#🅵-handle_name_conflict)
  - 🅵 [colorize](#🅵-colorize)
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
} #+.!|")
```


## Functions

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
## 🅵 colorize

```python
def colorize(docstring: str, color="red") -> str:
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
```


### 🅼 render

```python
def render(self, package: Package, output_path: Path | None = None) -> None:
```

Render the given package as Markdown. If output\_path is None or '-', output to stdout.

If output\_path is a directory, each module gets its own file; otherwise, all modules go into one file.
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
### 🅼 render\_class\_toc

```python
def render_class_toc(
    self, module: Module, cls: Class, indent: int
) -> list[str]:
```

Render a TOC entry for a class and its nested classes.
### 🅼 render\_class\_details

```python
def render_class_details(self, cls: Class, level: int) -> list[str]:
```

Render detailed documentation for a class including its signature, docstring details,

its methods, and any nested classes.
### 🅼 render\_function

```python
def render_function(
    self, func: Function, level: int, flag=FUNC_FLAG
) -> list[str]:
```

Render detailed documentation for a function/method including its signature and

docstring details \(parameters, returns, raises, etc.\).
### 🅼 render\_docstring

```python
def render_docstring(
    self, doc: docstring_parser.Docstring, indent: int = 0, simple=True
) -> list[str]:
```

Render detailed docstring information including description, parameters,

returns, raises, and attributes. An indent level can be provided for nested output.
### 🅼 link

```python
def link(self, module: Module, item: DocumentedItem | None = None) -> str:
```

Generate a link to a fully qualified name.
