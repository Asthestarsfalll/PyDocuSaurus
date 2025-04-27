#!/usr/bin/env python3
"""
This script crawls a Python package directory, extracts docstrings from modules,
classes, functions, methods, and constants using the `ast` module, and stores them in the associated data classes.

Additional features:
  - For each __init__.py, if an __all__ is defined, an exports list is generated.
  - Headers have HTML anchors derived from the fully qualified names.
  - For each function/method, its signature is included with type hints (if present) and its return type.
  - Autodetects docstring formats (Google-style, NumPy-style, etc.) and reformats them into Markdown.
  - Constants are detected and their types are included when available.
  - Parameter and return sections now include type information when available.
"""

from __future__ import annotations

import argparse
from pathlib import Path
from .models import Package
from .parse import parse_module
from .render import MarkdownRenderer


def crawl_package(package_path: Path, include_private: bool = False) -> Package:
    """Recursively crawl the package directory, parsing each .py file as a Module.

    If include_private is False, items (functions, classes, constants, submodules)
    whose names start with a single underscore (but not dunder names like __init__)
    are excluded.
    """
    pkg_name = package_path.name
    package = Package(
        path=package_path, name=pkg_name, fully_qualified_name=pkg_name, modules=[]
    )
    modules = []
    for file_path in package_path.glob("*.py"):
        if (
            not include_private
            and file_path.stem.startswith("_")
            and not file_path.stem.startswith("__")
        ):
            continue
        module = parse_module(file_path, package.fully_qualified_name, include_private)
        if module.name == "__init__":
            modules.append(module)

    # Add all modules to the package (including nested)
    while modules:
        module = modules.pop()
        package.modules.append(module)
        modules.extend(module.submodules)

    # Sort package.modules by fully_qualified_name
    package.modules.sort(key=lambda m: m.fully_qualified_name)

    return package


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Crawl a Python package and extract docstrings into Markdown."
    )
    parser.add_argument("package_path", help="Path to the Python package directory")
    parser.add_argument(
        "output_path",
        help="Path to write the Markdown file(s)"
        "Can be a directory or a single file. If a directory, each module will get its own file.",
    )
    parser.add_argument(
        "--include-private",
        action="store_true",
        help="Include private functions, classes, and constants (names starting with '_')",
    )
    parser.add_argument(
        "--no-runtime",
        action="store_false",
        help="Use runtime information",
    )
    args = parser.parse_args()
    package_dir = Path(args.package_path)

    if not package_dir.is_dir():
        print(f"Error: {package_dir} is not a directory.")
        return

    package = crawl_package(package_dir, include_private=args.include_private)
    renderer = MarkdownRenderer()

    output_path = Path(args.output_path)
    renderer.render(package, output_path, args.no_runtime)


if __name__ == "__main__":
    main()
