"""
QUESTION:
Write a function `longest_common_prefix` that takes a list of strings as input and returns the longest common prefix among all the strings. The function should have a time complexity of O(n * m), where n is the number of strings and m is the average length of the strings. If the input list is empty, the function should return an empty string. The function should not use any built-in string manipulation methods such as `find()`, `startswith()`, or slicing.
"""

def longest_common_prefix(strings):
    if not strings:
        return ""  # Return empty string if the set of strings is empty

    # Find the minimum length of the strings
    min_length = min(len(string) for string in strings)
    
    # Iterate through each character in the minimum length of the strings
    for i in range(min_length):
        # Check if the character at position i is the same in all strings
        if any(string[i] != strings[0][i] for string in strings):
            return strings[0][:i]  # Return the prefix if characters differ
    
    return strings[0][:min_length]  # Return the minimum length prefix