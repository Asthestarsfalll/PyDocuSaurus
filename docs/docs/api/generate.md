---
title: generate
sidebar_position: 3
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

<details>

<summary>crawl\_package</summary>
```python
def crawl_package(package_path: Path, include_private: bool = False) -> Package:
    pkg_name = package_path.name
    package = Package(
        path=package_path,
        name=pkg_name,
        fully_qualified_name=pkg_name,
        modules=[],
    )
    modules = []
    for file_path in package_path.glob("*.py"):
        if (
            not include_private
            and file_path.stem.startswith("_")
            and not file_path.stem.startswith("__")
        ):
            continue
        module = parse_module(
            file_path, package.fully_qualified_name, include_private
        )
        if module.name == "__init__":
            modules.append(module)
    while modules:
        module = modules.pop()
        package.modules.append(module)
        modules.extend(module.submodules)
    package.modules.sort(key=lambda m: m.fully_qualified_name)
    return package
```

</details>


Recursively crawl the package directory, parsing each .py file as a Module.

If include\_private is False, items \(functions, classes, constants, submodules\)
whose names start with a single underscore \(but not dunder names like \_\_init\_\_\)
are excluded.
## 🅵 main

```python
def main() -> None:
```
