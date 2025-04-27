---
title: models
sidebar_position: 3
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

<details>

<summary>Package</summary>
```python
@dataclass
class Package:
    path: Path = None
    name: str = None
    fully_qualified_name: str = None
    modules: list[Module] = field(default_factory=list)
```

</details>

## 🅲 Module

<details>

<summary>Module</summary>
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

</details>

## 🅲 Class

<details>

<summary>Class</summary>
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

</details>

## 🅲 Function

<details>

<summary>Function</summary>
```python
@dataclass
class Function:
    path: Path = None
    name: str = None
    fully_qualified_name: str = None
    signature: str = None
    docstring: docstring_parser.Docstring | None = None
    decorator_list: list[str] = field(default_factory=list)
    body: str | None = None
```

</details>

## 🅲 Constant

<details>

<summary>Constant</summary>
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

</details>
