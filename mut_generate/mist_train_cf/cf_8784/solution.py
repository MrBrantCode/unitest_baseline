"""
QUESTION:
Write a function called `add_excellent` that adds the string 'excellent' to the end of a given list. The function should have a time complexity of O(n) and should not use any built-in append or extend methods. The list may contain duplicates and has a maximum length of 1000. The function should handle cases where the list is empty or contains only one element, and it should not create any new data structures. If the list has already reached its maximum length, the function should print a message indicating that the list cannot be modified.
"""

def add_excellent(input_list):
    """
    Adds the string 'excellent' to the end of a given list.
    
    Args:
    input_list (list): The list to which 'excellent' is to be added.
    
    Returns:
    list: The list with 'excellent' added at the end.
    """
    max_length = 1000
    if len(input_list) == max_length:
        print("List has reached maximum length and cannot be modified.")
        return input_list
    else:
        last_index = len(input_list)
        input_list[last_index:last_index] = ['excellent']
        return input_list