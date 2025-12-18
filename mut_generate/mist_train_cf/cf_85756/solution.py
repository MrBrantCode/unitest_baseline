"""
QUESTION:
Design a function named `reverse_sort_exclude` that accepts two string parameters: `s` and `unwanted`. The function should return a string that contains the characters of `s` sorted in reverse lexicographic order, excluding all instances of the alphabetic characters contained within `unwanted`, considering both their uppercase and lowercase forms. The result should be devoid of any spaces. The solution must not use in-built Python functions for string reversals, sorting, or case conversions.
"""

def reverse_sort_exclude(s, unwanted):
    chars = [c for c in s if (c.lower() not in unwanted.lower() and c.upper() not in unwanted.upper() and c != ' ')]

    for i in range(len(chars)):
        for j in range(len(chars) - i - 1):
            if chars[j] < chars[j + 1]:    # If current character is smaller than the next
                chars[j], chars[j + 1] = chars[j + 1], chars[j]    # Swap them

    res = ''
    for char in chars:
        res += char

    return res