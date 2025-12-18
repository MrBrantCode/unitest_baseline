"""
QUESTION:
Write a function named `join_strings` that takes two strings `string1` and `string2` as input and returns a single string with `string2` in the middle of `string1` but reversed. The time complexity should be O(n) and the space complexity should be O(n), where n is the length of the longer string.
"""

def entance(string1, string2):
    # Reverse the second string
    reversed_string2 = string2[::-1]
    
    # Determine the length of the longer string
    n = max(len(string1), len(string2))
    
    # Create a list to store the characters of the final string
    result = []
    
    # Iterate through each index from 0 to n-1
    for i in range(n):
        # If the index is within the range of the first string, add its character to the result
        if i < len(string1):
            result.append(string1[i])
        # If the index is within the range of the reversed second string, add its character to the result
        if i < len(reversed_string2):
            result.append(reversed_string2[i])
    
    # Convert the list of characters to a string
    return "".join(result)