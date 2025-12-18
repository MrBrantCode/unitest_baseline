"""
QUESTION:
Implement a function named `is_valid_css_selector` that takes a string as input and returns `True` if the string is a valid CSS selector for CSS3, and `False` otherwise. The function should follow the CSS3 selector syntax rules to determine validity. The input string should be checked against these rules to select HTML elements in a webpage.
"""

import re

def is_valid_css_selector(selector):
    pattern = r'^[.#]?[a-zA-Z_][\w-]*(:\w+)?(\s+[>+~]\s*[.#]?[a-zA-Z_][\w-]*(:\w+)?)*$'
    return re.match(pattern, selector) is not None