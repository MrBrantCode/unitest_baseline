"""
QUESTION:
Write a function `convert_list_to_integers` that takes a list of strings as input, converts the strings that represent integers to integers, removes any duplicates, and returns a sorted list of integers in ascending order. If the input list is empty, print an error message and exit the function.
"""

def convert_list_to_integers(strings):
    """
    This function takes a list of strings, converts strings that represent integers to integers, 
    removes duplicates, and returns a sorted list of integers in ascending order.
    
    Args:
        strings (list): A list of strings.
    
    Returns:
        list: A sorted list of integers in ascending order.
    """
    if not strings:
        print("Error: input list is empty.")
        return
    
    integers = [int(string) for string in strings if string.isdigit()]
    return sorted(list(set(integers)))