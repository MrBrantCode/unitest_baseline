"""
QUESTION:
Create a function `repeater` that recursively prints a given string `s` `m` times. In each recursive call, the first and last letters of the string should be removed before printing. The initial length of `s` must be at least `m` characters. If `m` is 0 or the string becomes empty, the recursion should stop.
"""

def repeater(s: str, m: int) -> None:
    if m == 0 or len(s) <= 0:
        return
    else:
        print(s)
        repeater(s[1:-1], m-1)