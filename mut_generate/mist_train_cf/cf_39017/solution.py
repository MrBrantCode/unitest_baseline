"""
QUESTION:
Implement the function `process_string(s: str) -> Tuple[bool, bool]` that processes a string character by character. The function should track two boolean indicators: `bs` indicating whether a backslash `\` has been encountered, and `hy` indicating whether a hyphen `-` not preceded by a backslash has been encountered. The function should return a tuple of the `bs` and `hy` indicators after processing the entire input string `s`. The `bs` indicator is set to `True` when a backslash is encountered and remains `True` for subsequent characters, while the `hy` indicator is set to `True` when a hyphen is encountered and not preceded by a backslash.
"""

from typing import Tuple

def process_string(s: str) -> Tuple[bool, bool]:
    bs = False  
    hy = False  

    for ch in s:
        if ch == "\\":
            if not bs:
                bs = True  
            continue
        elif ch == "-" and not bs:
            hy = True  

    return bs, hy