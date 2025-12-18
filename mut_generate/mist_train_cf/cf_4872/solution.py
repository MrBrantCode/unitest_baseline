"""
QUESTION:
Write a function `is_greater` that takes two strings `string1` and `string2` as input and returns a boolean value indicating whether `string1` is lexicographically greater than `string2`. The comparison should be case-sensitive and no built-in functions or libraries for string comparison can be used.
"""

def is_greater(string1, string2):
    if len(string1) > len(string2):
        return True
    elif len(string1) < len(string2):
        return False
    
    for i in range(len(string1)):
        if ord(string1[i]) > ord(string2[i]):
            return True
        elif ord(string1[i]) < ord(string2[i]):
            return False
    
    return False