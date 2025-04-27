---
title: models
---

## TOC

- **Classes:**
  - 🅲 [DocumentedItem](#🅲-documenteditem)
  - 🅲 [Package](#🅲-package)
  - 🅲 [Module](#🅲-module)
  - 🅲 [Class](#🅲-class)
  - 🅲 [Function](#🅲-function)
  - 🅲 [Constant](#🅲-constant)

## Classes

## 🅲 DocumentedItem

```python
class DocumentedItem(Protocol):
    name: str = None
    fully_qualified_name: str = None
```
## 🅲 Package

```python
@dataclass
class Package:
    path: Path = None
    name: str = None
    fully_qualified_name: str = None
    modules: list[Module] = field(default_factory=list)
```
## 🅲 Module

```python
@dataclass
class Module:
    path: Path = None
    name: str = None
    fully_qualified_name: str = None
    submodules: list[Module] = field(default_factory=list)
    docstring: docstring_parser.Docstring | None = None
    constants: list[Constant] = field(default_factory=list)
    functions: list[Function] = field(default_factory=list)
    classes: list[Class] = field(default_factory=list)
    exports: list[str] = field(default_factory=list)
    aliases: dict[str, str] = field(default_factory=dict)
```
## 🅲 Class

```python
@dataclass
class Class:
    path: Path = None
    name: str = None
    fully_qualified_name: str = None
    signature: str = None
    docstring: docstring_parser.Docstring | None = None
    functions: list[Function] = field(default_factory=list)
    classes: list[Class] = field(default_factory=list)
    decorator_list: list[str] = field(default_factory=list)
    constants: list[Constant] = field(default_factory=list)
```
## 🅲 Function

```python
@dataclass
class Function:
    path: Path = None
    name: str = None
    fully_qualified_name: str = None
    signature: str = None
    docstring: docstring_parser.Docstring | None = None
    decorator_list: list[str] = field(default_factory=list)
```
## 🅲 Constant

```python
@dataclass
class Constant:
    path: Path = None
    name: str = None
    fully_qualified_name: str = None
    value: str = None
    type: str | None = None
    comment: str | None = None
```
