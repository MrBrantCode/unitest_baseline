"""
QUESTION:
Write a function `is_happy(s)` that determines whether a given string `s` is happy or not. A string is regarded as happy if it meets the following conditions: 
- it is at least 3 characters long
- each consecutive set of 3 characters are distinct
- every unique character appears at least twice, but not more than four times
- no character appears thrice in a consecutive sequence
- no character occurs both at the beginning and the end of the string
"""

def is_happy(s):
    # Checking the first condition - string must be at least 3 characters long
    if len(s) < 3:
        return False

    # Third condition - every unique character appears at least twice, but not more than four times
    char_count = {char: s.count(char) for char in set(s)} 
    for count in char_count.values():
        if count < 2 or count > 4:
            return False
    
    # Checking the second condition - each consecutive set of 3 characters are distinct
    for i in range(len(s) - 2):
        if len(set(s[i:i+3])) != 3:
            return False

    # Checking the fourth condition - no character appears thrice in consecutive sequence
    for i in range(len(s) - 2):
        if s[i] == s[i+1] == s[i+2]:
            return False

    # Integrating the new condition - no character to be allowed to occur both at the beginning and the end of the string
    if s[0] == s[-1]:
        return False

    # If it passes all conditions
    return True