from docstring_parser.google import Section, SectionType


FUNC_FLAG = "🅵"
CLASS_FLAG = "🅲"
MODULE_FLAG = "🅼"
ATTR_FLAG = "🅰"
INDEX_TEMPLATE = """---
title: {}
---

"""
DOCUSAURUS_SECTION = {
    "note": Section("Note", "note", SectionType.SINGULAR_OR_MULTIPLE),
    "info": Section("Info", "info", SectionType.SINGULAR_OR_MULTIPLE),
    "warn": Section("Warn", "warn", SectionType.SINGULAR_OR_MULTIPLE),
    "tip": Section("Tip", "tip", SectionType.SINGULAR_OR_MULTIPLE),
}
