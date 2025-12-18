"""
QUESTION:
Complete the code which should return `true` if the given object is a single ASCII letter (lower or upper case), `false` otherwise.
"""

def is_single_ascii_letter(s: str) -> bool:
    return len(s) == 1 and s.isalpha()