"""
QUESTION:
Write a function named `reverse_strings` that takes a list of strings as input and returns a new list where each string is reversed. The function should handle strings containing special characters and numbers. The function should not modify the original list.
"""

def reverse_strings(lst):
    """
    This function takes a list of strings as input and returns a new list where each string is reversed.
    
    The function handles strings containing special characters and numbers.
    
    The function does not modify the original list.
    
    Parameters:
    lst (list): A list of strings.
    
    Returns:
    list: A new list with each string reversed.
    """
    reversed_lst = []
    for string in lst:
        reversed_string = string[::-1]
        reversed_lst.append(reversed_string)
    return reversed_lst