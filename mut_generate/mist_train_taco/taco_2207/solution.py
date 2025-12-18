"""
QUESTION:
Example

Input

acmicpc
tsukuba


Output

No
"""

def can_form_string(s: str, t: str) -> bool:
    j = 0
    i = 0
    while i < len(t) and j < len(s):
        if t[i] == s[j]:
            j += 2
        i += 1
    return j >= len(s)