"""
QUESTION:
Write a function `extract_subtype_super_entity` that takes a code snippet as input and returns a tuple containing the subtype and super-entity information. The subtype is denoted by the `SUBTYPE OF` keyword followed by the subtype name within parentheses, and the super-entity is denoted by the `SUPER-ENTITY` keyword followed by the super-entity name within parentheses. The function should handle variations in the position and formatting of these elements within the code snippet and return a message indicating that the information was not found if either the subtype or super-entity cannot be extracted.
"""

import re

def extract_subtype_super_entity(code_snippet):
    subtype_pattern = r'SUBTYPE\s+OF\s+\(\s*(\w+)\s*\)'
    super_entity_pattern = r'SUPER-ENTITY\s*\(\s*(\w+)\s*\)'

    subtype_match = re.search(subtype_pattern, code_snippet)
    super_entity_match = re.search(super_entity_pattern, code_snippet)

    if subtype_match and super_entity_match:
        subtype = subtype_match.group(1)
        super_entity = super_entity_match.group(1)
        return subtype, super_entity
    else:
        return "Subtype and/or super-entity information not found in the code snippet."