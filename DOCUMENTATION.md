# Documentation

## Table of Contents

- [`python_docstring_markdown`](#python-docstring-markdown)
- [`__main__`](#main)
- [`generate`](#generate)
  - [`generate.make_anchor`](#generate-make-anchor)
  - [`generate.add_header`](#generate-add-header)
  - [`generate.get_module_name`](#generate-get-module-name)
  - [`generate.extract_all_from_ast`](#generate-extract-all-from-ast)
  - [`generate.get_function_signature`](#generate-get-function-signature)
  - [`generate.format_docstring`](#generate-format-docstring)
  - [`generate.extract_docstrings_from_node`](#generate-extract-docstrings-from-node)
  - [`generate.process_file`](#generate-process-file)
  - [`generate.crawl`](#generate-crawl)
  - [`generate.generate_toc`](#generate-generate-toc)
  - [`generate.generate_exports_section`](#generate-generate-exports-section)
  - [`generate.main`](#generate-main)

## Exports

- [`python_docstring_markdown`](#python-docstring-markdown):
  - [`crawl`](#generate-crawl)

<a id="python-docstring-markdown"></a>
# `python_docstring_markdown`


<a id="main"></a>
# `__main__`


<a id="generate"></a>
# `generate`

generate.py

This script crawls a Python package directory, extracts docstrings from modules,
classes, functions, and methods using the `ast` module, and writes the results
to a single Markdown file.

Additional features:
  - Module names are shown as dotted names (e.g. "foo.bar.baz") rather than file paths.
  - For each __init__.py, if an __all__ is defined, an Exports section is generated.
  - The Table of Contents lists fully qualified names (e.g. foo.bar.MyClass.my_method) without prefixes.
  - Headers have descriptive HTML anchors derived from their dotted names.
  - For each function/method, its signature is included with type hints (if present) and its return type.
  - Autodetects docstring formats (Google-style, NumPy-style, etc.) and reformats them into Markdown.
  - The Exports section builds links to the documented sections by matching the actual headers.

<a id="generate-make-anchor"></a>
## `generate.make_anchor`

```python
def make_anchor(text):
```

Create a slug for the anchor by removing formatting,

lower-casing, and replacing non-alphanumeric characters with hyphens.

<a id="generate-add-header"></a>
## `generate.add_header`

```python
def add_header(header_text, level):
```

Create a markdown header with a unique, descriptive anchor and record it for the TOC.

**Args:**

- `header_text` (*str*): The header text (expected to be a fully qualified dotted name).
- `level` (*int*): The markdown header level (1 for h1, 2 for h2, etc.)

**Returns:** (*list of str*) Markdown lines for the header (including an HTML anchor).

<a id="generate-get-module-name"></a>
## `generate.get_module_name`

```python
def get_module_name(file_path, package_dir):
```

Convert a file path to a dotted module name relative to package_dir.

For example, if package_dir is '/path/to/src' and file_path is
'/path/to/src/foo/bar/baz.py', the returned module name is 'foo.bar.baz'.
For __init__.py, the "__init__" part is dropped.

**Args:**

- `file_path` (*str*): The absolute or relative file path.
- `package_dir` (*str*): The root package directory.

**Returns:** (*str*) The dotted module name.

<a id="generate-extract-all-from-ast"></a>
## `generate.extract_all_from_ast`

```python
def extract_all_from_ast(tree):
```

Look for an assignment to __all__ in the module AST and extract its value.

**Args:**

- `tree` (*ast.Module*): The parsed AST of the module.

**Returns:** (*list of str or None*) The list of exported names if found, otherwise None.

<a id="generate-get-function-signature"></a>
## `generate.get_function_signature`

```python
def get_function_signature(node):
```

Build a string representation of the function/method signature,

including parameter type hints and the return type.

Note: Default values are not included.

**Args:**

- `node` (*ast.FunctionDef or ast.AsyncFunctionDef*): The function node.

**Returns:** (*str*) A signature string, e.g.:
def func(arg1: int, arg2: str, *args: Any, **kwargs: Any) -> bool:

<a id="generate-format-docstring"></a>
## `generate.format_docstring`

```python
def format_docstring(docstring):
```

Parse a docstring and reformat its components as Markdown.

**Args:**

- `docstring` (*str*): The raw docstring.

**Returns:** (*str*) The formatted Markdown version of the docstring.

<a id="generate-extract-docstrings-from-node"></a>
## `generate.extract_docstrings_from_node`

```python
def extract_docstrings_from_node(node, parent_qualname, heading_level):
```

Recursively extract docstrings from an AST node using fully qualified dotted names.

For functions and methods, the signature (with type hints) is included.
Docstrings are parsed (as Google-style) and reformatted into Markdown.

**Args:**

- `node` (*ast.AST*): The AST node (e.g. Module, ClassDef, FunctionDef).
- `parent_qualname` (*str*): The fully qualified name of the parent (module or class).
- `heading_level` (*int*): The markdown header level to use.

**Returns:** (*list of str*) Lines of markdown documenting the node.

<a id="generate-process-file"></a>
## `generate.process_file`

```python
def process_file(file_path, package_dir):
```

Process a single Python file to extract its documentation as markdown text.

If the file is an __init__.py, also extract its __all__.

**Args:**

- `file_path` (*str*): The path to the Python (.py) file.
- `package_dir` (*str*): The root package directory (used for computing module name).

**Returns:** (*str*) The markdown-formatted documentation extracted from the file.

<a id="generate-crawl"></a>
## `generate.crawl`

```python
def crawl(directory):
```

Recursively crawl a directory, process each Python file, and concatenate

their markdown documentation.

**Args:**

- `directory` (*str*): The root directory to crawl.

**Returns:** (*str*) The combined markdown documentation for the entire package.

<a id="generate-generate-toc"></a>
## `generate.generate_toc`

```python
def generate_toc():
```

Generate a Markdown-formatted Table of Contents based on the collected headers.

**Returns:** (*list of str*) Lines for the Table of Contents.

<a id="generate-generate-exports-section"></a>
## `generate.generate_exports_section`

```python
def generate_exports_section():
```

Generate a Markdown section listing __all__ exports for modules that define it.

Each module and export is linked to its respective section.

**Returns:** (*list of str*) Lines for the Exports section.

<a id="generate-main"></a>
## `generate.main`

```python
def main():
```
