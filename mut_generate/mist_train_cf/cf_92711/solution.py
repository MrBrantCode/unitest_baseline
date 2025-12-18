"""
QUESTION:
Implement the `collapse_repeating_chars` function that takes a string `s` of lowercase alphabetic characters and returns a new string where all consecutive repeating characters are collapsed into a single character, maintaining the original order of characters.
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