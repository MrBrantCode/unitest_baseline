"""
QUESTION:
Create a function `count_occurrences` that takes two strings `string1` and `string2` as input. The function should return the number of times `string1` is found within `string2` in a case-insensitive manner. If `string2` is empty, the function should return -1.
"""

def count_occurrences(string1, string2):
    if string2 == "":
        return -1
    
    string1 = string1.lower()
    string2 = string2.lower()
    
    count = 0
    for i in range(len(string2) - len(string1) + 1):
        if string2[i:i+len(string1)] == string1:
            count += 1
    
    return count