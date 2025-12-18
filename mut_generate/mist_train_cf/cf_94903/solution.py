"""
QUESTION:
Create a function named `reverse_string` that takes a string as input and reverses its order without using built-in string manipulation functions or libraries. The function must use a loop or iteration to achieve this, and it is not allowed to create any new variables or data structures other than the necessary function parameters and loop/index variables.
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