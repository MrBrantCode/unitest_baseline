"""
QUESTION:
Design a `NameObject` class with methods `set_name(name)`, `get_name()`, `calculate_length()`, `convert_to_uppercase()`, and `is_palindrome()`. The `set_name(name)` method should set the name of the object if the length of the name does not exceed 50 characters. The `get_name()` method should return the current name of the object. The `calculate_length()` method should return the length of the current name. The `convert_to_uppercase()` method should return the current name in uppercase. The `is_palindrome()` method should return `True` if the name is the same when its characters are reversed, ignoring whitespace, punctuation, and case.
"""

import re

def is_palindrome(name):
    cleaned_name = re.sub(r"[^\w]", "", name.lower())
    return cleaned_name == cleaned_name[::-1]