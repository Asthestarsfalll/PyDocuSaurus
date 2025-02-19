# Documentation

## Table of Contents

- [`python_docstring_markdown`](#python-docstring-markdown)
  - [`__main__`](#python-docstring-markdown-main)
  - [`generate`](#python-docstring-markdown-generate)
    - [`make_anchor`](#python-docstring-markdown-generate-make-anchor)
    - [`add_header`](#python-docstring-markdown-generate-add-header)
    - [`get_module_name`](#python-docstring-markdown-generate-get-module-name)
    - [`extract_all_from_ast`](#python-docstring-markdown-generate-extract-all-from-ast)
    - [`get_function_signature`](#python-docstring-markdown-generate-get-function-signature)
    - [`format_docstring`](#python-docstring-markdown-generate-format-docstring)
    - [`extract_docstrings_from_node`](#python-docstring-markdown-generate-extract-docstrings-from-node)
    - [`process_file`](#python-docstring-markdown-generate-process-file)
    - [`crawl`](#python-docstring-markdown-generate-crawl)
    - [`generate_toc`](#python-docstring-markdown-generate-generate-toc)
    - [`main`](#python-docstring-markdown-generate-main)

<a id="python-docstring-markdown"></a>
# `python_docstring_markdown`


<a id="python-docstring-markdown-main"></a>
## `__main__`


<a id="python-docstring-markdown-generate"></a>
## `generate`

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

<a id="python-docstring-markdown-generate-make-anchor"></a>
### `make_anchor`

```python
def make_anchor(text):
```

Create a slug for the anchor by removing formatting,

lower-casing, and replacing non-alphanumeric characters with hyphens.

<a id="python-docstring-markdown-generate-add-header"></a>
### `add_header`

```python
def add_header(full_header_text, provided_level):
```

Create a markdown header with a unique, descriptive anchor and record it for the TOC.

Instead of printing the full dotted name, only the stem (last segment) is used
for display.

**Args:**

- `full_header_text` (*str*): The fully qualified dotted name.
- `provided_level` (*int*): The markdown header level to use.

**Returns:** (*list of str*) Markdown lines for the header (including an HTML anchor).

<a id="python-docstring-markdown-generate-get-module-name"></a>
### `get_module_name`

```python
def get_module_name(file_path, package_dir):
```

Convert a file path to a dotted module name relative to package_dir,

including the package’s base name.
For example, if package_dir is '/path/to/sample_package' and file_path is
'/path/to/sample_package/core.py', the returned module name is 'sample_package.core'.
For __init__.py, the "__init__" part is dropped.

<a id="python-docstring-markdown-generate-extract-all-from-ast"></a>
### `extract_all_from_ast`

```python
def extract_all_from_ast(tree):
```

Look for an assignment to __all__ in the module AST and extract its value.

**Args:**

- `tree` (*ast.Module*): The parsed AST of the module.

**Returns:** (*list of str or None*) The list of exported names if found, otherwise None.

<a id="python-docstring-markdown-generate-get-function-signature"></a>
### `get_function_signature`

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

<a id="python-docstring-markdown-generate-format-docstring"></a>
### `format_docstring`

```python
def format_docstring(docstring):
```

Parse a docstring and reformat its components as Markdown.

**Args:**

- `docstring` (*str*): The raw docstring.

**Returns:** (*str*) The formatted Markdown version of the docstring.

<a id="python-docstring-markdown-generate-extract-docstrings-from-node"></a>
### `extract_docstrings_from_node`

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

<a id="python-docstring-markdown-generate-process-file"></a>
### `process_file`

```python
def process_file(file_path, package_dir):
```

Process a single Python file to extract its documentation as markdown text.

If the file is an __init__.py, also extract its __all__.

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

<a id="python-docstring-markdown-generate-generate-toc"></a>
### `generate_toc`

```python
def generate_toc():
```

Generate a Markdown-formatted Table of Contents.

The TOC uses the stored full name (to compute indentation based on the number of dots)
while displaying only the stem name.

<a id="python-docstring-markdown-generate-main"></a>
### `main`

```python
def main():
```
