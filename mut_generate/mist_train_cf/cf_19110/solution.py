"""
QUESTION:
Create a function `maxLengthSubstring` that finds the length of the longest substring without repeating characters in a given string, considering whitespace characters as potential repeating characters. The function should handle cases with special characters, numbers, and alphanumeric characters. The input is a string, and the output should be the length of the longest substring without repeating characters.
"""

def maxLengthSubstring(s: str) -> int:
    """
    Finds the length of the longest substring without repeating characters in a given string.

    Args:
    s (str): The input string.

    Returns:
    int: The length of the longest substring without repeating characters.
    """
    
    # Initialize a variable "maxLength" to 0 to keep track of the length of the longest substring without repeating characters.
    maxLength = 0
    
    # Initialize an empty dictionary "charMap" to store the last occurrence index of each character encountered.
    charMap = {}
    
    # Initialize two pointers "start" and "end" to mark the start and end of the current substring.
    start = 0
    end = 0
    
    # Iterate over each character "c" in the given string:
    while end < len(s):
        c = s[end]
        
        # If "c" is in the "charMap" and its last occurrence index is after the "start" pointer:
        if c in charMap and charMap[c] >= start:
            # Update "start" to the index after the last occurrence index of "c" in the "charMap".
            start = charMap[c] + 1
        
        # Add "c" to the "charMap" with its index as the value.
        charMap[c] = end
        
        # Calculate the length of the current substring by subtracting "start" from "end" (inclusive).
        current_length = end - start + 1
        
        # Update "maxLength" to the maximum between "maxLength" and the length of the current substring.
        maxLength = max(maxLength, current_length)
        
        # Set "end" to the next index.
        end += 1
    
    # Return "maxLength".
    return maxLength