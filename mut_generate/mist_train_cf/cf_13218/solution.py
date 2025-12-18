"""
QUESTION:
Implement a function `collapse_repeating_chars(s)` that takes a string of lowercase alphabetic characters as input and returns a new string where all consecutive repeating characters are collapsed to a single character, maintaining the original order.
"""

def collapse_repeating_chars(s):
    # Initialize an empty string to store the collapsed characters
    result = ""
    
    # Iterate through each character in the input string
    for i in range(len(s)):
        # If the current character is the first occurrence or is different from the previous character,
        # add it to the result string
        if i == 0 or s[i] != s[i-1]:
            result += s[i]
    
    return result