# python-docstring-markdown

A Python tool that generates Markdown documentation from Python module docstrings. It automatically creates a table of contents, tracks module exports (`__all__`), and docstrings into clean Markdown.

## Features

- Generates a table of contents with anchor links
- Auto-detects ReST, Google, Numpydoc-style and Epydoc docstrings
- Includes function signatures with type hints
- Tracks and documents module exports (`__all__`)
- Preserves module hierarchy in documentation
- Handles nested classes and functions

## Installation

```bash
pip install python-docstring-markdown
```

## Usage

### Command Line

```bash
python -m python_docstring_markdown <package_dir> <output_file>
```

Arguments:
- `package_dir`: Path to your Python package directory
- `output_file`: Path where the Markdown documentation file will be saved

Example:
```bash
python -m python_docstring_markdown ./src/my_package docs/api.md
```

### Python API

```python
from python_docstring_markdown import crawl

# Generate documentation for a package
docs_content = crawl("./src/my_package")

# Save to a file
with open("docs/api.md", "w") as f:
    f.write(docs_content)
```

## Documentation Format

The generated documentation includes:

1. A table of contents with links to all sections
2. An exports section listing all `__all__` declarations
3. Module documentation organized hierarchically
4. Function signatures with type hints
5. Formatted docstrings preserving:
   - Description
   - Arguments
   - Returns
   - Raises
   - Examples

## License

CC-0 1.0 Universal. See the [LICENSE](LICENSE) file for more information.