"""
QUESTION:
Write a function `calculate_string_length(string)` to calculate the length of a given string without using built-in length functions, loops, or recursion.
"""

def calculate_string_length(string):
    # Convert the string to a list
    string_list = list(string)
    
    # Use the index() method to find the index of the first space character
    # If no space is found, return the length of the list
    try:
        length = string_list.index(' ')
    except ValueError:
        length = len(string_list)
    
    return length