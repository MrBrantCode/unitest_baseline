"""
QUESTION:
Write a function `find_first_non_repeating_char` that takes a string as input and returns the first non-repeating character in the string. The function should have a time complexity of O(n) and should not use any additional data structures. The function should be case-sensitive. If there are no non-repeating characters in the string, the function should return -1.
"""

def find_first_non_repeating_char(s):
    result = ''
    repeated = ''
    for c in s:
        if c in repeated:
            continue
        if c in result:
            result = result.replace(c, '')
            repeated += c
        else:
            result += c
    return -1 if not result else result[0]