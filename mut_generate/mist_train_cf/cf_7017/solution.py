"""
QUESTION:
Write a function `find_first_non_repeating_char` that finds the first non-repeating character in a given string. The solution should have a time complexity of O(n), not use any additional data structures beyond strings, be case-sensitive, and handle strings containing special characters. If the string contains no non-repeating characters, the function should return -1.
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
    
    if result == "":
        return -1
    
    return result[0]