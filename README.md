# PyDocuSaurus


Adapted from [python-docstring-markdown](https://github.com/criccomini/python-docstring-markdown)

A Python module and CLI that walks a Python package/directory and outputs a **Docusaurus Style** Markdown files from all docstrings in the package.


## TODO

- [x] Fix the links in module exports
- [ ] Colorize the parameters, returns and riaises item
- [ ] Supports for other Docusaurus features
- [ ] More configurable
- [ ] Auto translation

## Features

- Crawls the packages, modules, classes, functions, and methods using the `ast` module
- Generate the structured Markdown documentation for all docstrings in the package
- Auto-detects ReST, Google, Numpydoc-style and Epydoc docstrings using [`docstring-parser-fork`](https://pypi.org/project/docstring-parser-fork/)
- Generates a table of contents with links
- Tracks and documents module exports (`__all__`)
- Preserves module hierarchy in documentation
- Handles nested classes and functions
- Docusaurus features supported, for instance, Admonitions(Note, Warning, Important and Tip), markdown metadata.

## Installation

```bash
pip install PyDocuSaurus
```

## Usage

### Command Line

```bash
pdocs <package_dir> <output_dir>
```

Arguments:
- `package_dir`: Path to your Python package directory
- `output_dir`: Path where the Markdown documentation file will be saved
- `--include-private`: Include private members in the documentation

Example:
```bash
pdocs ./src/my_package docs/api/
```

## Documentation


## Contributing

I welcome feedback and contributions!

## License

CC-0 1.0 Universal. See the [LICENSE](LICENSE) file for more information.
