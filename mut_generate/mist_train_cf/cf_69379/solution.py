"""
QUESTION:
Write a function called `findNonRepeatingChar` that finds the first non-repeating character in a given string. The function should return the first non-repeating character if found, otherwise return None. Assume the input string contains only lowercase letters.
"""

def findNonRepeatingChar(string):
    char_count = {}
    
    for char in string:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    
    for char in string:
        if char_count[char] == 1:
            return char
    
    return None