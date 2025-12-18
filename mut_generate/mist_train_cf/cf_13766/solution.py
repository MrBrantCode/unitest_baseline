"""
QUESTION:
Write a function `find_first_non_repeating_char` that takes a string as input and returns the first non-repeating character in the string. The function should have a time complexity of O(n) and should not use any additional data structures besides the input string and a few variables. The solution should be case-sensitive and return None if no such character exists.
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