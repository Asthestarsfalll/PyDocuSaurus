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
    "method": FUNC_FLAG,
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


class Return:
    pass
