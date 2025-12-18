"""
QUESTION:
Implement a function `remove_occurrences(s, t)` that takes two strings `s` and `t` as input and returns a string with all occurrences of `t` removed from `s`. The removal should be case-sensitive, meaning that it should differentiate between uppercase and lowercase characters.
"""

def remove_occurrences(s, t):
    # Initialize an empty result string
    result = ""
    
    # Initialize a variable to keep track of the current position in string s
    i = 0
    
    # Loop through string s
    while i < len(s):
        # Check if the substring starting from the current position matches string t
        if s[i:i+len(t)] == t:
            # Move the current position forward by the length of string t
            i += len(t)
        else:
            # Append the current character to the result string and move to the next character
            result += s[i]
            i += 1
    
    return result