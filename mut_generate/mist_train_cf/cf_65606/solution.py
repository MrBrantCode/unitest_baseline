"""
QUESTION:
Create a function called `check_sorted` that takes a list as input and returns a string indicating whether the list is sorted in ascending or descending order. The function should work with lists containing different data types (such as integers, floats, strings) and should be able to handle null or undefined values. The function should also be able to handle nested lists by comparing the first element of each sublist, and if the first elements are equal, it should consider the next element and so on. The function should return an error message if the input list is not sorted.

Note: Due to the complexity of determining the sorting algorithm and its time complexity, the function will only focus on determining the order of the sorted list.
"""

def check_sorted(input_list):
    """
    This function checks if a list is sorted in ascending or descending order.
    
    Args:
        input_list (list): The list to be checked.
    
    Returns:
        str: A string indicating the order of the list, or an error message if the list is not sorted.
    """
    
    # Check if list is sorted in ascending order
    if all(input_list[i] <= input_list[i+1] for i in range(len(input_list)-1)):
        return "List is sorted in ascending order"
    
    # Check if list is sorted in descending order
    elif all(input_list[i] >= input_list[i+1] for i in range(len(input_list)-1)):
        return "List is sorted in descending order"
    
    # If list is neither sorted in ascending nor descending order
    else:
        return "List is not sorted"


def check_sorted_nested(input_list):
    """
    This function checks if a nested list is sorted based on the first element of each sublist.
    
    Args:
        input_list (list): The nested list to be checked.
    
    Returns:
        str: A string indicating the order of the list, or an error message if the list is not sorted.
    """
    
    # Check if each sublist has at least one element
    if not all(len(sublist) > 0 for sublist in input_list):
        return "Error: Each sublist must have at least one element."
    
    # Check if list is sorted in ascending order
    if all(input_list[i][0] <= input_list[i+1][0] for i in range(len(input_list)-1)):
        return "List is sorted in ascending order"
    
    # Check if list is sorted in descending order
    elif all(input_list[i][0] >= input_list[i+1][0] for i in range(len(input_list)-1)):
        return "List is sorted in descending order"
    
    # If list is neither sorted in ascending nor descending order
    else:
        return "List is not sorted"