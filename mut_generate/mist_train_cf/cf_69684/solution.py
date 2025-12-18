"""
QUESTION:
Create a function `verify_string(s: str)` that returns `True` if the input string `s` contains the words "hello" and "world" in any case, exactly once each, and as separate words (not part of another word), and `False` otherwise. The words "hello" and "world" do not have to be adjacent in the string.
"""

import re

def verify_string(s: str) -> bool:
    hello = [match for match in re.findall(r'\bhello\b', s, flags=re.IGNORECASE)]
    world = [match for match in re.findall(r'\bworld\b', s, flags=re.IGNORECASE)]

    return len(hello) == len(world) == 1