"""
QUESTION:
Create a function called `replace_phrase_case_insensitive` that takes three parameters: `string`, `phrase`, and `new_string`. The function should replace all occurrences of the specified `phrase` in the `string` with `new_string`, ignoring case sensitivity and only replacing if it is a complete word.
"""

import re

def replace_phrase_case_insensitive(string, phrase, new_string):
    return re.sub(r'\b' + re.escape(phrase) + r'\b', new_string, string, flags=re.IGNORECASE)