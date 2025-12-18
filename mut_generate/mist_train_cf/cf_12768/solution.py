"""
QUESTION:
Implement a function named `remove_duplicates` that takes an array of strings as input and returns an array with only unique strings, maintaining the original order of the strings. The function should be efficient enough to handle large input arrays of up to 100,000 elements.
"""

def remove_duplicates(arr):
    unique_strings = set()
    result = []
    
    for string in arr:
        if string not in unique_strings:
            result.append(string)
            unique_strings.add(string)
    
    return result