"""
QUESTION:
Write a function named `reverse_string` that takes a string as input and returns the reversed string without using any built-in string manipulation functions or libraries. The function should use a loop or iteration and should not create any new variables or data structures.
"""

def reverse_string(s):
    # Convert string to character array
    s = list(s)
    
    # Initialize pointers
    start = 0
    end = len(s) - 1
    
    # Reverse the characters in-place
    while start < end:
        # Swap characters
        s[start], s[end] = s[end], s[start]
        
        # Increment start and decrement end
        start += 1
        end -= 1
    
    # Convert character array back to string
    return ''.join(s)