"""
QUESTION:
Write a function `reverse_string(s)` that takes a string `s` consisting of at most 1000 lowercase letters as input and returns a new string with the same set of characters in reverse order without using built-in reverse functions or methods and string manipulation functions.
"""

def reverse_string(s):
    # Convert the string to a list since strings are immutable in Python
    char_list = list(s)
    
    # Initialize two pointers
    left = 0
    right = len(s) - 1
    
    # Swap characters until the pointers meet in the middle
    while left < right:
        char_list[left], char_list[right] = char_list[right], char_list[left]
        left += 1
        right -= 1
    
    # Convert the list back to a string and return it
    return ''.join(char_list)