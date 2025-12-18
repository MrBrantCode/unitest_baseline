"""
QUESTION:
Write a function `find_first_non_repeating_char` that finds the first non-repeating character in a given string. The function should have a time complexity of O(n) and cannot use any additional data structures beyond a constant number of variables. The function should be case-sensitive and return the first non-repeating character, or None if no such character exists.
"""

def find_first_non_repeating_char(string):
    result = ""
    repeated = ""
    
    for c in string:
        if c in repeated:
            continue
        if c in result:
            result = result.replace(c, "")
            repeated += c
        else:
            result += c
    
    return result[0] if result else None