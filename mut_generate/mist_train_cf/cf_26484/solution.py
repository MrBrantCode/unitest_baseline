"""
QUESTION:
Write a function `decode_text(chars, recognized_chars)` that takes a set of characters `chars` and a list of recognized characters `recognized_chars`, and returns the decoded text. The function should exclude duplicate characters and only consider characters present in `chars`. The CTC-blank character is not included in `recognized_chars`.
"""

from typing import Set, List

def decode_text(chars: Set[str], recognized_chars: List[str]) -> str:
    decoded_text = ''
    prev_char = None
    for char in recognized_chars:
        if char != prev_char and char in chars:
            decoded_text += char
        prev_char = char
    return decoded_text