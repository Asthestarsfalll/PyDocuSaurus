---
title: parse
---

## TOC

- **Functions:**
  - 🅵 [should\_include](#🅵-should_include) - Returns True if the given name should be included based on the value
  - 🅵 [get\_string\_value](#🅵-get_string_value) - Extract a string from an AST node representing a constant.
  - 🅵 [get\_import\_from](#🅵-get_import_from)
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

```python
def should_include(name: str, include_private: bool) -> bool:
```

Returns True if the given name should be included based on the value

of include\_private. Always include dunder names like \_\_init\_\_.
## 🅵 get\_string\_value

```python
def get_string_value(node: ast.AST) -> str | None:
```

Extract a string from an AST node representing a constant.
## 🅵 get\_import\_from

```python
def get_import_from(imported_name: str, module_ast: ast.Module):
```
## 🅵 build\_signature

```python
def build_signature(node: ast.FunctionDef | ast.AsyncFunctionDef) -> str:
```

Construct a signature string for a function/method from its AST node.
## 🅵 parse\_function

```python
def parse_function(
    node: ast.FunctionDef | ast.AsyncFunctionDef,
    file_path: Path,
    parent: Class | Module,
    type: str = "function",
) -> Function:
```

Parse a function or method node into a Function dataclass instance.
## 🅵 parse\_class

```python
def parse_class(
    node: ast.ClassDef,
    parent: Module | Class,
    file_path: Path,
    include_private: bool,
    code: str,
) -> Class:
```

Parse a class node into a Class dataclass instance and process its methods and nested classes.
## 🅵 parse\_module\_docstring

```python
def parse_module_docstring(
    module_ast: ast.Module,
) -> docstring_parser.Docstring | None:
```

Extract and parse the module docstring.
## 🅵 parse\_module\_exports

```python
def parse_module_exports(
    module_ast: ast.Module,
) -> tuple[list[str], dict[str, str]]:
```

Extract \_\_all\_\_ exports from an \_\_init\_\_.py module if present and parse import aliases.

**Returns:**

- **[tuple](https://docs.python.org/3/library/stdtypes.html#tuples)**: A tuple containing:
- list of exported names from \_\_all\_\_
- dictionary mapping original names to their aliases \(from 'import as'\)
## 🅵 \_get\_comment\_of\_constants

```python
def _get_comment_of_constants(code: str, line_number: int) -> str | None:
```
## 🅵 parse\_constants

```python
def parse_constants(node, code, module, file_path, include_private, cache=True):
```
## 🅵 parse\_module\_constants

```python
def parse_module_constants(
    code: str,
    module_ast: ast.Module,
    module: Module,
    file_path: Path,
    include_private: bool,
) -> None:
```

Parse constants defined in a module.

A constant is considered any assignment at module level whose target is a Name in ALL CAPS,
excluding \_\_all\_\_. Supports both regular assignments \(with optional type comments\)
and annotated assignments.
## 🅵 parse\_module\_functions

```python
def parse_module_functions(
    module_ast: ast.Module,
    module: Module,
    file_path: Path,
    include_private: bool,
) -> None:
```

Parse top-level functions in a module.
## 🅵 parse\_module\_classes

```python
def parse_module_classes(
    code: str,
    module_ast: ast.Module,
    module: Module,
    file_path: Path,
    include_private: bool,
) -> None:
```

Parse classes in a module.
## 🅵 parse\_module\_submodules

```python
def parse_module_submodules(
    module: Module, file_path: Path, include_private: bool
) -> None:
```

Parse submodules of a module.
## 🅵 parse\_module

```python
def parse_module(
    file_path: Path, fully_qualified_name: str, include_private: bool
) -> Module:
```

Parse a single module file into a Module dataclass instance.
