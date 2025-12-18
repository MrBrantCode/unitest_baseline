"""
QUESTION:
Write a function named `flatten_unique` that takes a two-dimensional list as input and returns a one-dimensional list containing unique elements from the input list. The function should ignore any duplicate elements and maintain the original order of elements. The input list can contain any type of elements, but for simplicity, assume it only contains integers. The function should not use any external libraries or built-in functions to remove duplicates or flatten the list.
"""

def flatten_unique(two_dimensional_list):
    """
    This function takes a two-dimensional list as input, 
    flattens it, and returns a one-dimensional list containing unique elements.
    
    Args:
        two_dimensional_list (list): A list of lists containing elements of any type.
    
    Returns:
        list: A one-dimensional list containing unique elements from the input list.
    """
    unique_elements = []
    for sublist in two_dimensional_list:
        for element in sublist:
            if element not in unique_elements:
                unique_elements.append(element)
    return unique_elements