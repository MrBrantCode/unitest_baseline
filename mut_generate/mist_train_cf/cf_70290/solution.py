"""
QUESTION:
Write a function `find_last_occurrence(S: str, p: str) -> int` that takes a string `S` and a pattern `p` as input and returns the index of the last occurrence of `p` in `S`. If `p` is not found in `S`, the function should return -1. The function should consider that string indices are 0-based.
"""

def find_last_occurrence(S: str, p: str) -> int:
    try:
        return S.rindex(p)
    except ValueError:
        return -1