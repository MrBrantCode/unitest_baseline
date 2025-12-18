"""
QUESTION:
Implement a function named `is_valid_css_selector` that checks whether a given string is a valid CSS selector for CSS3. The function should return `True` if the string follows the CSS3 selector syntax rules and `False` otherwise. The CSS3 selector syntax rules include matching the start and end of the string, handling optional `.` or `#` characters at the beginning, and allowing for HTML tag names, pseudo-class selectors, and combinators (`+`, `>`, or `~`).
"""

import re

def is_valid_css_selector(selector):
    # CSS3 selector syntax rules
    pattern = r'^[.#]?[a-zA-Z_][\w-]*(:\w+)?(\s+[>+~]\s*[.#]?[a-zA-Z_][\w-]*(:\w+)?)*$'
    return re.match(pattern, selector) is not None