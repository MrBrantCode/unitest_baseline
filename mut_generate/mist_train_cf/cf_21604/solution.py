"""
QUESTION:
Write a function named `reverse_string` that takes a string `s` as input, reverses the characters in the string without using any built-in reverse functions, and returns the reversed string. The function should not use extra memory and should handle the fact that strings are immutable in Python.
"""

def reverse_string(s):
    # Convert the string to a list since strings are immutable in Python
    s = list(s)
    start = 0
    end = len(s) - 1
    
    while start < end:
        # Swap characters at start and end pointers
        s[start], s[end] = s[end], s[start]
        
        # Move the pointers towards each other
        start += 1
        end -= 1
    
    # Convert the list back to a string and return
    return ''.join(s)