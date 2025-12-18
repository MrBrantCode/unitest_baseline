"""
QUESTION:
Write a function named `switch_string` that takes a string as input and returns the string with its two parts switched. The index to split the string should be determined by the following rules: 
- If the string length is odd, split at the index of the middle character.
- If the string length is even, split at the index of the second character from the middle.
"""

def switch_string(s):
    length = len(s)
    if length % 2 == 1:
        index = length // 2
    else:
        index = length // 2 + 1
    
    part1 = s[:index]
    part2 = s[index:]
    
    return part2 + part1