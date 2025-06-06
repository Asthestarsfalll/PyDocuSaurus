---
title: constants
sidebar_position: 3
---

## TOC

- **Attributes:**
  - 🅰 [FUNC\_FLAG](#🅰-func_flag) - flag for func
  - 🅰 [CLASS\_FLAG](#🅰-class_flag) - flag for class
  - 🅰 [MODULE\_FLAG](#🅰-module_flag) - flag for module
  - 🅰 [METHOD\_FLAG](#🅰-method_flag) - flag for method
  - 🅰 [ATTR\_FLAG](#🅰-attr_flag) - flag for attribute
  - 🅰 [UNKNOWN\_FLAG](#🅰-unknown_flag) - flag for unknown
  - 🅰 [FLAG\_STR\_MAPPING](#🅰-flag_str_mapping)
  - 🅰 [FLAG\_EXPLAIN](#🅰-flag_explain)
  - 🅰 [INDEX\_TEMPLATE](#🅰-index_template)
  - 🅰 [MAX\_LINES](#🅰-max_lines)
  - 🅰 [INCLUDE\_LINES](#🅰-include_lines)
  - 🅰 [INCLUDE\_IF](#🅰-include_if)
  - 🅰 [DETAIL\_TEMPLATE\_BEGINE](#🅰-detail_template_begine)
  - 🅰 [DETAIL\_TEMPLATE\_END](#🅰-detail_template_end)
  - 🅰 [DOCUSAURUS\_SECTION](#🅰-docusaurus_section) - for docusaurus annotations
  - 🅰 [OBJECT\_CACHE](#🅰-object_cache) - name: \{fully\_qualified\_name: type\}
  - 🅰 [COMMON\_TYPE\_LINKS](#🅰-common_type_links) - numeric-types-int-float-complex",
- **Classes:**
  - 🅲 [Return](#🅲-return)

## Attributes

## 🅰 FUNC\_FLAG

```python
FUNC_FLAG = """🅵""" #flag for func
```

## 🅰 CLASS\_FLAG

```python
CLASS_FLAG = """🅲""" #flag for class
```

## 🅰 MODULE\_FLAG

```python
MODULE_FLAG = """🅜""" #flag for module
```

## 🅰 METHOD\_FLAG

```python
METHOD_FLAG = """🅼""" #flag for method
```

## 🅰 ATTR\_FLAG

```python
ATTR_FLAG = """🅰""" #flag for attribute
```

## 🅰 UNKNOWN\_FLAG

```python
UNKNOWN_FLAG = """🅤""" #flag for unknown
```

## 🅰 FLAG\_STR\_MAPPING

<details>

<summary>FLAG\_STR\_MAPPING</summary>
```python
FLAG_STR_MAPPING = {
    "class": CLASS_FLAG,
    "function": FUNC_FLAG,
    "module": MODULE_FLAG,
    "constant": ATTR_FLAG,
    "method": METHOD_FLAG,
}
```

</details>


## 🅰 FLAG\_EXPLAIN

<details>

<summary>FLAG\_EXPLAIN</summary>
```python
FLAG_EXPLAIN = """**Flags:**
- 🅵: function
- 🅲: class
- 🅼: method
- 🅜: module
- 🅰: attribute
- 🅤: unknown

"""
```

</details>


## 🅰 INDEX\_TEMPLATE

<details>

<summary>INDEX\_TEMPLATE</summary>
```python
INDEX_TEMPLATE = """---
title: {}
sidebar_position: {}
---

"""
```

</details>


## 🅰 MAX\_LINES

```python
MAX_LINES = 25
```

## 🅰 INCLUDE\_LINES

```python
INCLUDE_LINES = 20
```

## 🅰 INCLUDE\_IF

```python
INCLUDE_IF = True
```

## 🅰 DETAIL\_TEMPLATE\_BEGINE

```python
DETAIL_TEMPLATE_BEGINE = """<details>

<summary>{}</summary>"""
```

## 🅰 DETAIL\_TEMPLATE\_END

```python
DETAIL_TEMPLATE_END = """
</details>
"""
```

## 🅰 DOCUSAURUS\_SECTION

<details>

<summary>DOCUSAURUS\_SECTION</summary>
```python
DOCUSAURUS_SECTION = {
    "note": Section("Note", "note", SectionType.SINGULAR_OR_MULTIPLE),
    "info": Section("Info", "info", SectionType.SINGULAR_OR_MULTIPLE),
    "danger": Section("Danger", "danger", SectionType.SINGULAR_OR_MULTIPLE),
    "warning": Section("Warning", "warning", SectionType.SINGULAR_OR_MULTIPLE),
    "tip": Section("Tip", "tip", SectionType.SINGULAR_OR_MULTIPLE),
} #for docusaurus annotations
```

</details>


## 🅰 OBJECT\_CACHE

```python
OBJECT_CACHE: dict[dict[str, str]] = defaultdict(lambda: {}) #name: {fully_qualified_name: type}
```

## 🅰 COMMON\_TYPE\_LINKS

<details>

<summary>COMMON\_TYPE\_LINKS</summary>
```python
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
    "Any": (
        "https://docs.python.org/3/library/typing.html#typing.Any",
        "typing.Any",
    ),
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
    "Set": (
        "https://docs.python.org/3/library/typing.html#typing.Set",
        "typing.Set",
    ),
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
    "OSError": (
        "https://docs.python.org/3/library/exceptions.html#OSError",
        "OSError",
    ),
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
    "TypeError": (
        "https://docs.python.org/3/library/exceptions.html#TypeError",
        "TypeError",
    ),
    "UnboundLocalError": (
        "https://docs.python.org/3/library/exceptions.html#UnboundLocalError",
        "UnboundLocalError",
    ),
    "FunctionType": (
        "https://docs.python.org/3/library/types.html#types.FunctionType",
        "FunctionType",
    ),
    "ModuleType": (
        "https://docs.python.org/3/library/types.html#types.ModuleType",
        "ModuleType",
    ),
    "None": ("https://docs.python.org/3/library/constants.html#None", "None"),
    "inspect.Parameter": (
        "https://docs.python.org/3/library/inspect.html#inspect.Parameter",
        "Parameter",
    ),
    "inspect.Signature": (
        "https://docs.python.org/3/library/inspect.html#inspect.Signature",
        "Signature",
    ),
    "inspect.ParameterKind": (
        "https://docs.python.org/3/library/inspect.html#inspect.ParameterKind",
        "ParameterKind",
    ),
    "inspect.Section": (
        "https://docs.python.org/3/library/inspect.html#inspect.Section",
        "Section",
    ),
    "inspect.SectionType": (
        "https://docs.python.org/3/library/inspect.html#inspect.SectionType",
        "SectionType",
    ),
    "inspect.SINGULAR": (
        "https://docs.python.org/3/library/inspect.html#inspect.SINGULAR",
        "SINGULAR",
    ),
    "Sequence": (
        "https://docs.python.org/3/library/typing.html#typing.Sequence",
        "Sequence",
    ),
} #numeric-types-int-float-complex",
```

</details>



## Classes

## 🅲 Return

```python
class Return:
```
