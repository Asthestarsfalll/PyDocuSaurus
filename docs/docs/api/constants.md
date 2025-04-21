---
title: constants
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
  - 🅰 [DOCUSAURUS\_SECTION](#🅰-docusaurus_section) - for docusaurus annotations
  - 🅰 [OBJECT\_CACHE](#🅰-object_cache) - name: \{fully\_qualified\_name: type\}
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

```python
FLAG_STR_MAPPING = {
    "class": CLASS_FLAG,
    "function": FUNC_FLAG,
    "module": MODULE_FLAG,
    "constant": ATTR_FLAG,
    "method": FUNC_FLAG,
}
```

## 🅰 FLAG\_EXPLAIN

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

## 🅰 INDEX\_TEMPLATE

```python
INDEX_TEMPLATE = """---
title: {}
---

"""
```

## 🅰 DOCUSAURUS\_SECTION

```python
DOCUSAURUS_SECTION = {
    "note": Section("Note", "note", SectionType.SINGULAR_OR_MULTIPLE),
    "info": Section("Info", "info", SectionType.SINGULAR_OR_MULTIPLE),
    "warn": Section("Warn", "warn", SectionType.SINGULAR_OR_MULTIPLE),
    "tip": Section("Tip", "tip", SectionType.SINGULAR_OR_MULTIPLE),
} #for docusaurus annotations
```

## 🅰 OBJECT\_CACHE

```python
OBJECT_CACHE: dict[dict[str, str]] = defaultdict(lambda: {}) #name: {fully_qualified_name: type}
```


## Classes

## 🅲 Return

```python
class Return:
```
