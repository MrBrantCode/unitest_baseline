"""
QUESTION:
Write a function `reverse_order` that takes a string as input and returns the string with the order of its words reversed, while preserving the positions of special characters. The function should ignore non-alphabetic characters and swap alphabetic characters from the start and end of the string, moving towards the center.
"""

def reverse_order(string):
    string = list(string)
 
    # Initialize left and right pointers
    left = 0
    right = len(string) - 1
 
    while left < right:
 
        # Ignore special characters
        if not string[left].isalpha():
            left += 1
        elif not string[right].isalpha():
            right -= 1
        else:
            # Swap characters
            string[left], string[right] = string[right], string[left]
            left += 1
            right -= 1
 
    return ''.join(string)