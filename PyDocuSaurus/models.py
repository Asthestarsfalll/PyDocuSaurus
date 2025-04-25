from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path
from typing import Protocol
import docstring_parser


class DocumentedItem(Protocol):
    name: str
    fully_qualified_name: str


@dataclass
class Package:
    path: Path
    name: str  # final name (directory name)
    fully_qualified_name: str  # same as name for the top-level package
    modules: list[Module] = field(default_factory=list)


@dataclass
class Module:
    path: Path
    # final module name (file stem)
    name: str
    # e.g. package_name.module or just package_name for __init__
    fully_qualified_name: str
    submodules: list[Module] = field(default_factory=list)
    docstring: docstring_parser.Docstring | None = None
    constants: list[Constant] = field(default_factory=list)
    functions: list[Function] = field(default_factory=list)
    classes: list[Class] = field(default_factory=list)
    exports: list[str] = field(default_factory=list)
    aliases: dict[str, str] = field(default_factory=dict)


@dataclass
class Class:
    path: Path
    # final class name
    name: str
    # e.g. foo.bar.Baz
    fully_qualified_name: str
    signature: str
    docstring: docstring_parser.Docstring | None = None
    functions: list[Function] = field(default_factory=list)
    classes: list[Class] = field(default_factory=list)  # For nested classes


@dataclass
class Function:
    path: Path
    name: str  # final function/method name
    fully_qualified_name: str  # e.g. foo.bar.Baz.method
    signature: str
    docstring: docstring_parser.Docstring | None = None


@dataclass
class Constant:
    path: Path
    name: str  # constant name
    fully_qualified_name: str  # e.g. foo.bar.MY_CONSTANT
    value: str  # the string representation of the value
    type: str | None = None  # the constant's type, if available
    comment: str | None = None  # the constant's docstring, if available
