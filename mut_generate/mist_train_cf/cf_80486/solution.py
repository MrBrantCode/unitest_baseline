"""
QUESTION:
Write a function `alternate_case_concat(s1, s2)` that takes two strings `s1` and `s2` as input and returns their concatenation with alternating cases, starting with a capital letter. The function should preserve non-alphabetical characters in their original case.
"""

def alternate_case_concat(s1, s2):
    s = s1+s2
    result = ''
    upper = True
    for char in s:
        if char.isalpha():
            if upper:
                result += char.upper()
            else:
                result += char.lower()
            upper = not upper
        else:
            result += char
    return result