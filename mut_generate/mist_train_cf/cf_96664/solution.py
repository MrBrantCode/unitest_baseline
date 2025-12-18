"""
QUESTION:
Write a function `reverse_string(s)` that takes a string `s` as input and reverses its characters without using any built-in reverse functions or extra memory. The function should return the reversed string. Note that strings in Python are immutable, so the function should convert the string to a mutable data structure to swap its characters.
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