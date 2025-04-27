---
title: generate
---

This script crawls a Python package directory, extracts docstrings from modules,

classes, functions, methods, and constants using the \`ast\` module, and stores them in the associated data classes.

Additional features:
  - For each \_\_init\_\_.py, if an \_\_all\_\_ is defined, an exports list is generated.
  - Headers have HTML anchors derived from the fully qualified names.
  - For each function/method, its signature is included with type hints \(if present\) and its return type.
  - Autodetects docstring formats \(Google-style, NumPy-style, etc.\) and reformats them into Markdown.
  - Constants are detected and their types are included when available.
  - Parameter and return sections now include type information when available.

## TOC

- **Functions:**
  - 🅵 [crawl\_package](#🅵-crawl_package) - Recursively crawl the package directory, parsing each .py file as a Module.
  - 🅵 [main](#🅵-main)

## Functions

## 🅵 crawl\_package

```python
def crawl_package(package_path: Path, include_private: bool = False) -> Package:
```

Recursively crawl the package directory, parsing each .py file as a Module.

If include\_private is False, items \(functions, classes, constants, submodules\)
whose names start with a single underscore \(but not dunder names like \_\_init\_\_\)
are excluded.
## 🅵 main

```python
def main() -> None:
```
