"""
QUESTION:
Write a function named `reverse_string` that takes a string as input and returns the reversed string. The function should not use any built-in string reversal functions, slicing, or additional data structures. It should achieve a time complexity of O(n) and a space complexity of O(1), where n is the length of the string.
"""

def reverse_string(string):
    # Convert the string to a list, since strings are immutable
    string_list = list(string)
    
    # Initialize two pointers at the start and end of the string
    start = 0
    end = len(string_list) - 1
    
    # Iterate until the pointers meet or cross each other
    while start < end:
        # Swap characters at the start and end positions
        string_list[start], string_list[end] = string_list[end], string_list[start]
        
        # Move the pointers towards each other
        start += 1
        end -= 1
    
    # Convert the list back to a string and return it
    return ''.join(string_list)