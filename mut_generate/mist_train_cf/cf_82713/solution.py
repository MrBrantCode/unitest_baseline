"""
QUESTION:
Implement a function `calculate_product` that takes a list of numbers as input and returns the product of all the numeric elements in the list. The function should handle potential cases where the list contains non-numeric data by ignoring these elements and continuing with the numeric elements. The input list can contain both integers and floating-point numbers.
"""

def calculate_product(num_list):
    """
    Calculate the product of all numeric elements in a given list.
    
    This function iterates through the input list, ignores non-numeric data, 
    and returns the product of the numeric elements.
    
    Args:
        num_list (list): A list containing numeric and/or non-numeric data.
    
    Returns:
        float: The product of the numeric elements in the list.
    """
    product = 1
    for num in num_list:
        try:
            product *= num
        except TypeError:
            print("Non-numeric data encountered in the list. Can only handle integers and floats.")
    return product