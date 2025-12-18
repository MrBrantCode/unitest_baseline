"""
QUESTION:
Write a function `count_strings` that takes a list of strings as input and returns a dictionary where the keys are the alphanumeric strings from the input list and the values are their respective counts. The function should only consider alphanumeric strings and ignore strings containing numbers or special characters. The function should not use any built-in Python functions or libraries, except for the `isalnum()` method, and should have a time complexity of O(n^2).
"""

def count_strings(strings):
    counts = {}
    
    for string in strings:
        # Ignore strings with numbers or special characters
        if not string.isalnum():
            continue
        
        # Count the string
        if string in counts:
            counts[string] += 1
        else:
            counts[string] = 1
    
    return counts