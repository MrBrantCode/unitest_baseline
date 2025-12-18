"""
QUESTION:
Implement a `TextSource` class with `__init__` and `read` methods. The `__init__` method should initialize the `contents` and `offset`. The `read` method takes a regular expression pattern, matches it against the `contents` starting from the current `offset`, and updates the `offset` if a match is found. If a match is found, return the matched object; otherwise, return `None`. The `offset` should be an integer representing the current position in the `contents` string. The `contents` should be a string and the regular expression pattern should be of type `re.Pattern`.
"""

import re
from typing import Optional

def read_pattern(text_source, regex: re.Pattern) -> Optional[re.Match]:
    match = regex.match(text_source['contents'], text_source['offset'])
    if not match:
        return None
    text_source['offset'] = match.end()
    return match