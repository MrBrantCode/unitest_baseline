"""
QUESTION:
Write a function `replace_nth` that replaces the nth occurrence of a substring in a given string. The function should take four parameters: the original string `s`, the substring `old` to be replaced, the replacement string `new`, and the occurrence number `n`. The function should return the modified string with the nth occurrence of `old` replaced by `new`. If `n` is larger than the number of occurrences of `old` in `s`, the function should return the original string `s`.
"""

def replace_nth(s, old, new, n):
    parts = s.split(old, n)
    if len(parts) < n + 1:
        return s
    return old.join(parts[:-1]) + new + old.join(parts[-1:])