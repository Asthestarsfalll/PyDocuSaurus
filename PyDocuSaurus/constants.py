from docstring_parser.google import Section, SectionType


FUNC_FLAG = "🅵"  # flag for func
CLASS_FLAG = "🅲"  # flag for class
MODULE_FLAG = "🅼"  # flag for module
ATTR_FLAG = "🅰"  # flag for attribute

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
