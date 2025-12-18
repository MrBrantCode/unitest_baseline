"""
QUESTION:
Implement a function named `is_valid_bootstrap_navbar` that checks if a given HTML string contains a valid Bootstrap navbar component. The function should take a string `html_string` as input and return a boolean value. A valid Bootstrap navbar component should consist of a `<nav>` element with the class "navbar", a `<button>` element with the class "navbar-toggler", and a `<div>` element with the classes "collapse" and "navbar-collapse". The function should return `True` if the HTML string contains a valid Bootstrap navbar component, and `False` otherwise.
"""

import re

def is_valid_bootstrap_navbar(html_string: str) -> bool:
    pattern = r'<nav class="navbar">.*<button class="navbar-toggler"></button>.*<div class="collapse navbar-collapse"'
    match = re.search(pattern, html_string, re.DOTALL)
    return match is not None