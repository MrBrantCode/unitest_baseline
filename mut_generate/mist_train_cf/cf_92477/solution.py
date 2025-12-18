"""
QUESTION:
Implement a function named `remove_duplicates` that takes an array of strings as input and returns a new array containing only the unique strings from the original array, while maintaining their original order. The function should be able to handle large input arrays efficiently.
"""

def remove_duplicates(arr):
    unique_strings = set()
    result = []
    
    for string in arr:
        if string not in unique_strings:
            result.append(string)
            unique_strings.add(string)
    
    return result