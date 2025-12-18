"""
QUESTION:
Implement a function `firstNonRepeatingCharacter(s)` that finds the index position of the first non-repeating character in a given string `s`. The string is case-sensitive and contains only alphanumeric characters. If there are no unique characters, return -1. The function must not use built-in data structures like lists or dictionaries, but can use arrays and caching to handle multiple function calls efficiently.
"""

cache = {}
def firstNonRepeatingCharacter(s):
    if s in cache:
        return cache[s]
    
    count = [0]*256
    
    for char in s:
        count[ord(char)] += 1
    
    for i in range(len(s)):
        if count[ord(s[i])] == 1:
            cache[s] = i  
            return i
    
    cache[s] = -1  
    return -1