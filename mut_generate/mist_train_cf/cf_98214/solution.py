"""
QUESTION:
Write a function `two_longest_with_digit_and_special` that takes a list of strings as input and returns the two longest strings that contain at least one digit and one special character (@, !, #, $, %, ^, &, *, (, )).
"""

def two_longest_with_digit_and_special(lst):
    result = []
    longest = ""
    second_longest = ""
    for s in lst:
        if len(s) > len(longest):
            second_longest = longest
            longest = s
        elif len(s) > len(second_longest):
            second_longest = s
    for s in [longest, second_longest]:
        if any(c.isdigit() for c in s) and any(c in '@!#$%^&*()' for c in s):
            result.append(s)
    return result