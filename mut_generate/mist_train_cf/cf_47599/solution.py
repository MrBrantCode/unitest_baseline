"""
QUESTION:
Write a function `makeSpecial(s, foo)` that takes a string `s` and a substring `foo` as input. The function should return the string `s` with all occurrences of `foo` wrapped in a new span element with class "special". The function should not use any external libraries, only Python's built-in string functions. The function should work correctly for simple cases where `foo` is a plaintext substring without special characters that have meaning in HTML.
"""

def makeSpecial(s, foo):
    return s.replace(foo, '<span class="special">{}</span>'.format(foo))