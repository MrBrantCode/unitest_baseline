"""
QUESTION:
Write a function named `find_x_index` that uses a while loop to find the index of the letter 'x' in a given string. If the letter 'x' is found, return its index; otherwise, return a message indicating that 'x' was not found. Assume that the input string is not empty.
"""

def find_x_index(string):
    """
    This function finds the index of the letter 'x' in a given string.
    
    Args:
    string (str): The input string to search for 'x'.
    
    Returns:
    int or str: The index of 'x' if found, otherwise a message indicating 'x' was not found.
    """
    
    index = 0
    found_x = False
    
    while index < len(string):
        if string[index] == 'x':
            found_x = True
            break
        index += 1
    
    if found_x:
        return index
    else:
        return "The letter 'x' was not found in the string."