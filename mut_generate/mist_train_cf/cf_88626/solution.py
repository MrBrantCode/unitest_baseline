"""
QUESTION:
Create a function `count_strings` that takes a list of strings as input and returns a dictionary where the keys are the alphanumeric strings from the input list and the values are the number of times each alphanumeric string appears in the list. The function should only count alphanumeric strings and ignore strings that contain numbers or special characters, and it should have a time complexity of O(n^2) where n is the length of the input list.
"""

def count_strings(strings):
    counts = {}
    
    for string in strings:
        if not string.isalnum():
            continue
        
        if string in counts:
            counts[string] += 1
        else:
            counts[string] = 1
    
    return counts