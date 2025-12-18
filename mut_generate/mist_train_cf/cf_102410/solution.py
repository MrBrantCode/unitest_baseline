"""
QUESTION:
Create a function called `longest_strings` that takes an array of strings as input and returns a new array containing only the strings with the longest length. If there are multiple strings with the longest length, return all of them in the new array. The input array may be empty or contain only empty strings. The function should have a time complexity of O(n) and should not use any built-in sorting or searching functions.
"""

def longest_strings(arr):
    if not arr:
        return []
    
    longest_length = 0
    result = []
    
    for string in arr:
        if len(string) > longest_length:
            longest_length = len(string)
            result = [string]
        elif len(string) == longest_length:
            result.append(string)
    
    return result