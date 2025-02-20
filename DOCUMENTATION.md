# Documentation

## Table of Contents

- [`python_docstring_markdown`](#python-docstring-markdown)
  - [`__main__`](#python-docstring-markdown-main)
  - [`generate`](#python-docstring-markdown-generate)
    - [`crawl`](#python-docstring-markdown-generate-crawl)
    - [`main`](#python-docstring-markdown-generate-main)

<a id="python-docstring-markdown"></a>
# `python_docstring_markdown`


**Exports:**

- `crawl`

<a id="python-docstring-markdown-main"></a>
## `__main__`


<a id="python-docstring-markdown-generate"></a>
## `generate`

This script crawls a Python package directory, extracts docstrings from modules,

classes, functions, and methods using the `ast` module, and writes the results
to a single Markdown file.

Additional features:
  - Module names are shown as dotted names (e.g. "foo.bar.baz") rather than file paths.
  - For each __init__.py, if an __all__ is defined, an Exports section is generated.
  - Headers have descriptive HTML anchors derived from their dotted names.
  - For each function/method, its signature is included with type hints (if present) and its return type.
  - Autodetects docstring formats (Google-style, NumPy-style, etc.) and reformats them into Markdown.

<a id="python-docstring-markdown-generate-crawl"></a>
### `crawl`

```python
def crawl(directory):
```

Recursively crawl a directory, process each Python file, and generate

the complete markdown documentation.

**Args:**

- `directory` (*str*): The root directory to crawl.

**Returns:** (*str*) The complete markdown documentation for the entire package,
including table of contents and exports section.

<a id="python-docstring-markdown-generate-main"></a>
### `main`

```python
def main():
```
