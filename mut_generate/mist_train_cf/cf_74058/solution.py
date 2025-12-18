"""
QUESTION:
Create a function `checkSubstring` that takes three string arguments, `str_1`, `str_2`, and `str_3`. The function should return `True` if both `str_1` and `str_3` are substrings within `str_2`, and a specific message if either or both of them occur more than once in `str_2`. If either `str_1` or `str_3` is not a substring of `str_2`, the function should return `False`. The function should also handle strings containing whitespace and punctuation.
"""

def checkSubstring(str_1, str_2, str_3):
    occurs_str_1 = str_2.count(str_1)
    occurs_str_3 = str_2.count(str_3)
    
    if occurs_str_1 == 0 or occurs_str_3 == 0:
        return False
    elif occurs_str_1 > 1 and occurs_str_3 > 1:
        return "Both substrings occur more than once."
    elif occurs_str_1 > 1:
        return "str_1 occurs more than once."
    elif occurs_str_3 > 1:
        return "str_3 occurs more than once."
    else:
        return True