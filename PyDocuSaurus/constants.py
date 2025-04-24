from docstring_parser.google import Section, SectionType
from collections import defaultdict


FUNC_FLAG = "🅵"  # flag for func
CLASS_FLAG = "🅲"  # flag for class
MODULE_FLAG = "🅜"  # flag for module
METHOD_FLAG = "🅼"  # flag for method
ATTR_FLAG = "🅰"  # flag for attribute
UNKNOWN_FLAG = "🅤"  # flag for unknown
FLAG_STR_MAPPING = {
    "class": CLASS_FLAG,
    "function": FUNC_FLAG,
    "module": MODULE_FLAG,
    "constant": ATTR_FLAG,
    "method": METHOD_FLAG,
}
FLAG_EXPLAIN = """**Flags:**
- 🅵: function
- 🅲: class
- 🅼: method
- 🅜: module
- 🅰: attribute
- 🅤: unknown

"""

INDEX_TEMPLATE = """---
title: {}
---

"""
# Index template for docusaurus


DOCUSAURUS_SECTION = {
    "note": Section("Note", "note", SectionType.SINGULAR_OR_MULTIPLE),
    "info": Section("Info", "info", SectionType.SINGULAR_OR_MULTIPLE),
    "warn": Section("Warn", "warn", SectionType.SINGULAR_OR_MULTIPLE),
    "tip": Section("Tip", "tip", SectionType.SINGULAR_OR_MULTIPLE),
}  # for docusaurus annotations

OBJECT_CACHE: dict[dict[str, str]] = defaultdict(
    lambda: {}
)  # name: {fully_qualified_name: type}

COMMON_TYPE_LINKS = {
    "int": (
        "https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex",
        "__builtins__.int",
    ),
    "float": (
        "https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex",
        "__builtins__.float",
    ),
    "str": (
        "https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str",
        "__builtins__.str",
    ),
    "list": (
        "https://docs.python.org/3/library/stdtypes.html#lists",
        "__builtins__.list",
    ),
    "dict": (
        "https://docs.python.org/3/library/stdtypes.html#mapping-types-dict",
        "__builtins__.dict",
    ),
    "tuple": (
        "https://docs.python.org/3/library/stdtypes.html#tuples",
        "__builtins__.tuple",
    ),
    "set": (
        "https://docs.python.org/3/library/stdtypes.html#set-types-set-frozenset",
        "__builtins__.set",
    ),
    "frozenset": (
        "https://docs.python.org/3/library/stdtypes.html#set-types-set-frozenset",
        "__builtins__.frozenset",
    ),
    "bool": (
        "https://docs.python.org/3/library/stdtypes.html#boolean-values",
        "__builtins__.bool",
    ),
    "bytes": (
        "https://docs.python.org/3/library/stdtypes.html#bytes",
        "__builtins__.bytes",
    ),
    "bytearray": (
        "https://docs.python.org/3/library/stdtypes.html#bytearray-objects",
        "__builtins__.bytearray",
    ),
    "NoneType": (
        "https://docs.python.org/3/library/stdtypes.html#the-null-object",
        "__builtins__.None",
    ),
    "complex": (
        "https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex",
        "__builtins__.complex",
    ),
    "type": (
        "https://docs.python.org/3/library/functions.html#type",
        "__builtins__.type",
    ),
    "range": (
        "https://docs.python.org/3/library/stdtypes.html#range",
        "__builtins__.range",
    ),
    "slice": (
        "https://docs.python.org/3/library/functions.html#slice",
        "__builtins__.slice",
    ),
    "memoryview": (
        "https://docs.python.org/3/library/stdtypes.html#memoryview",
        "__builtins__.memoryview",
    ),
    "Any": ("https://docs.python.org/3/library/typing.html#typing.Any", "typing.Any"),
    "Union": (
        "https://docs.python.org/3/library/typing.html#typing.Union",
        "typing.Union",
    ),
    "Optional": (
        "https://docs.python.org/3/library/typing.html#typing.Optional",
        "typing.Optional",
    ),
    "List": (
        "https://docs.python.org/3/library/typing.html#typing.List",
        "typing.List",
    ),
    "Dict": (
        "https://docs.python.org/3/library/typing.html#typing.Dict",
        "typing.Dict",
    ),
    "Tuple": (
        "https://docs.python.org/3/library/typing.html#typing.Tuple",
        "typing.Tuple",
    ),
    "Set": ("https://docs.python.org/3/library/typing.html#typing.Set", "typing.Set"),
    "FrozenSet": (
        "https://docs.python.org/3/library/typing.html#typing.FrozenSet",
        "typing.FrozenSet",
    ),
    "Callable": (
        "https://docs.python.org/3/library/typing.html#typing.Callable",
        "typing.Callable",
    ),
    "TypeVar": (
        "https://docs.python.org/3/library/typing.html#typing.TypeVar",
        "typing.TypeVar",
    ),
    "Generic": (
        "https://docs.python.org/3/library/typing.html#typing.Generic",
        "typing.Generic",
    ),
    "NewType": (
        "https://docs.python.org/3/library/typing.html#typing.NewType",
        "typing.NewType",
    ),
    "NoReturn": (
        "https://docs.python.org/3/library/typing.html#typing.NoReturn",
        "typing.NoReturn",
    ),
    "Literal": (
        "https://docs.python.org/3/library/typing.html#typing.Literal",
        "typing.Literal",
    ),
    "TypedDict": (
        "https://docs.python.org/3/library/typing.html#typing.TypedDict",
        "typing.TypedDict",
    ),
    "Protocol": (
        "https://docs.python.org/3/library/typing.html#typing.Protocol",
        "typing.Protocol",
    ),
    "runtime_checkable": (
        "https://docs.python.org/3/library/typing.html#typing.runtime_checkable",
        "typing.runtime_checkable",
    ),
    "Final": (
        "https://docs.python.org/3/library/typing.html#typing.Final",
        "typing.Final",
    ),
    "ClassVar": (
        "https://docs.python.org/3/library/typing.html#typing.ClassVar",
        "typing.ClassVar",
    ),
    "Self": (
        "https://docs.python.org/3/library/typing.html#typing.Self",
        "typing.Self",
    ),
    "Unpack": (
        "https://docs.python.org/3/library/typing.html#typing.Unpack",
        "typing.Unpack",
    ),
    "TypeAlias": (
        "https://docs.python.org/3/library/typing.html#typing.TypeAlias",
        "typing.TypeAlias",
    ),
    "ExtensionType": (
        "https://www.tensorflow.org/api_docs/python/tf/experimental/ExtensionType",
        "tf.experimental.ExtensionType",
    ),
    "PyTypeObject": (
        "https://docs.python.org/3/c-api/type.html#c.PyTypeObject",
        "PyTypeObject",
    ),
    "PyType_Type": (
        "https://docs.python.org/3/c-api/type.html#c.PyType_Type",
        "PyType_Type",
    ),
    "PyType_Check": (
        "https://docs.python.org/3/c-api/type.html#c.PyType_Check",
        "PyType_Check",
    ),
    "PyType_FromSpec": (
        "https://docs.python.org/3/c-api/type.html#c.PyType_FromSpec",
        "PyType_FromSpec",
    ),
    "PyType_GetSlot": (
        "https://docs.python.org/3/c-api/type.html#c.PyType_GetSlot",
        "PyType_GetSlot",
    ),
    "RuntimeError": (
        "https://docs.python.org/3/library/exceptions.html#RuntimeError",
        "RuntimeError",
    ),
    "ValueError": (
        "https://docs.python.org/3/library/exceptions.html#ValueError",
        "ValueError",
    ),
    "AssertionError": (
        "https://docs.python.org/3/library/exceptions.html#AssertionError",
        "AssertionError",
    ),
    "AttributeError": (
        "https://docs.python.org/3/library/exceptions.html#AttributeError",
        "AttributeError",
    ),
    "KeyError": (
        "https://docs.python.org/3/library/exceptions.html#KeyError",
        "KeyError",
    ),
    "IndexError": (
        "https://docs.python.org/3/library/exceptions.html#IndexError",
        "IndexError",
    ),
    "NameError": (
        "https://docs.python.org/3/library/exceptions.html#NameError",
        "NameError",
    ),
    "SyntaxError": (
        "https://docs.python.org/3/library/exceptions.html#SyntaxError",
        "SyntaxError",
    ),
    "NotImplementedError": (
        "https://docs.python.org/3/library/exceptions.html#NotImplementedError",
        "NotImplementedError",
    ),
    "ModuleNotFoundError": (
        "https://docs.python.org/3/library/exceptions.html#ModuleNotFoundError",
        "ModuleNotFoundError",
    ),
    "FileExistsError": (
        "https://docs.python.org/3/library/exceptions.html#FileExistsError",
        "FileExistsError",
    ),
    "FileNotFoundError": (
        "https://docs.python.org/3/library/exceptions.html#FileNotFoundError",
        "FileNotFoundError",
    ),
    "IsADirectoryError": (
        "https://docs.python.org/3/library/exceptions.html#IsADirectoryError",
        "IsADirectoryError",
    ),
    "PermissionError": (
        "https://docs.python.org/3/library/exceptions.html#PermissionError",
        "PermissionError",
    ),
    "ProcessLookupError": (
        "https://docs.python.org/3/library/exceptions.html#ProcessLookupError",
        "ProcessLookupError",
    ),
    "ConnectionRefusedError": (
        "https://docs.python.org/3/library/exceptions.html#ConnectionRefusedError",
        "ConnectionRefusedError",
    ),
    "ConnectionResetError": (
        "https://docs.python.org/3/library/exceptions.html#ConnectionResetError",
        "ConnectionResetError",
    ),
    "BrokenPipeError": (
        "https://docs.python.org/3/library/exceptions.html#BrokenPipeError",
        "BrokenPipeError",
    ),
    "ChildProcessError": (
        "https://docs.python.org/3/library/exceptions.html#ChildProcessError",
        "ChildProcessError",
    ),
    "ConnectionAbortedError": (
        "https://docs.python.org/3/library/exceptions.html#ConnectionAbortedError",
        "ConnectionAbortedError",
    ),
    "ConnectionError": (
        "https://docs.python.org/3/library/exceptions.html#ConnectionError",
        "ConnectionError",
    ),
    "BlockingIOError": (
        "https://docs.python.org/3/library/exceptions.html#BlockingIOError",
        "BlockingIOError",
    ),
    "TimeoutError": (
        "https://docs.python.org/3/library/exceptions.html#TimeoutError",
        "TimeoutError",
    ),
    "StopIteration": (
        "https://docs.python.org/3/library/exceptions.html#StopIteration",
        "StopIteration",
    ),
    "GeneratorExit": (
        "https://docs.python.org/3/library/exceptions.html#GeneratorExit",
        "GeneratorExit",
    ),
    "EOFError": (
        "https://docs.python.org/3/library/exceptions.html#EOFError",
        "EOFError",
    ),
    "OSError": ("https://docs.python.org/3/library/exceptions.html#OSError", "OSError"),
    "WindowsError": (
        "https://docs.python.org/3/library/exceptions.html#WindowsError",
        "WindowsError",
    ),
    "OverflowError": (
        "https://docs.python.org/3/library/exceptions.html#OverflowError",
        "OverflowError",
    ),
    "ZeroDivisionError": (
        "https://docs.python.org/3/library/exceptions.html#ZeroDivisionError",
        "ZeroDivisionError",
    ),
    "ArithmeticError": (
        "https://docs.python.org/3/library/exceptions.html#ArithmeticError",
        "ArithmeticError",
    ),
    "FloatingPointError": (
        "https://docs.python.org/3/library/exceptions.html#FloatingPointError",
        "FloatingPointError",
    ),
    "RecursionError": (
        "https://docs.python.org/3/library/exceptions.html#RecursionError",
        "RecursionError",
    ),
    "SystemError": (
        "https://docs.python.org/3/library/exceptions.html#SystemError",
        "SystemError",
    ),
    "MemoryError": (
        "https://docs.python.org/3/library/exceptions.html#MemoryError",
        "MemoryError",
    ),
    "ReferenceError": (
        "https://docs.python.org/3/library/exceptions.html#ReferenceError",
        "ReferenceError",
    ),
    "BufferError": (
        "https://docs.python.org/3/library/exceptions.html#BufferError",
        "BufferError",
    ),
    "ImportError": (
        "https://docs.python.org/3/library/exceptions.html#ImportError",
        "ImportError",
    ),
}


class Return:
    pass
