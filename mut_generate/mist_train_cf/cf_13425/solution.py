"""
QUESTION:
Write a function `reverse_string(input_str)` that takes a string `input_str` as input and returns the reversed string without using any built-in string reversal functions or methods.
"""

def entrance(input_str):
    # Convert the string into a list
    char_list = list(input_str)
    
    # Define two pointers, one pointing to the start and the other pointing to the end of the list
    start = 0
    end = len(char_list) - 1
    
    # Swap characters from both ends until the pointers meet or cross each other
    while start < end:
        # Swap characters
        char_list[start], char_list[end] = char_list[end], char_list[start]
        
        # Move the pointers towards each other
        start += 1
        end -= 1
    
    # Convert the list back to a string
    reversed_str = ''.join(char_list)
    
    # Return the reversed string
    return reversed_str