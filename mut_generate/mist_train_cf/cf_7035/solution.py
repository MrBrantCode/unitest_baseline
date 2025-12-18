"""
QUESTION:
Write a function named `longest_common_prefix` that takes a list of strings as input and returns the longest common prefix among the strings. The function should have a time complexity of O(n * m), where n is the number of strings and m is the average length of the strings. If the input list is empty, the function should return an empty string. Do not use any built-in string manipulation methods such as `find()`, `startswith()`, or slicing.
"""

def entrance(strings):
    if not strings:
        return ""  

    min_length = min(len(string) for string in strings)
    
    for i in range(min_length):
        if any(string[i] != strings[0][i] for string in strings):
            return strings[0][:i]  
    
    return strings[0][:min_length]  