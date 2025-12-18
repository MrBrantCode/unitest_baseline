"""
QUESTION:
Implement a function `calculate_specificity(selector: str) -> List[int]` that takes a CSS selector as input and returns its specificity as a list of four integers representing the count of inline styles, IDs, classes/pseudo-classes/attribute selectors, and elements/pseudo-elements, respectively. Note that inline styles are not applicable in CSS selectors, so the count of inline styles should always be 0. IDs, classes, pseudo-classes, attribute selectors, elements, and pseudo-elements should be counted based on the following characters: `#`, `.`, `:`, `[`, and spaces (for elements). The function should handle cases where some components are not present in the selector by returning a count of 0 for those components.
"""

from typing import List

def calculate_specificity(selector: str) -> List[int]:
    inline_styles = selector.count("style=")
    ids = selector.count("#")
    classes_pseudo_attrs = selector.count(".") + selector.count(":") + selector.count("[")
    elements_pseudo_elements = selector.count(" ") + 1  

    return [inline_styles, ids, classes_pseudo_attrs, elements_pseudo_elements]