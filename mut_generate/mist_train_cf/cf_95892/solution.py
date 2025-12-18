"""
QUESTION:
Define a function `calculate_nested_list_product` that calculates the sum of the product of the elements of a nested list with up to three levels of nesting, where each element is a positive integer. The function should take a nested list as input and return the calculated sum.
"""

def calculate_nested_list_product(nested_list):
    """
    This function calculates the sum of the product of the elements of a nested list.
    
    Args:
    nested_list (list): A nested list with up to three levels of nesting, where each element is a positive integer.
    
    Returns:
    int: The calculated sum.
    """
    total_sum = 1
    nested_sum = 0
    
    def recursive_helper(nested_list):
        nonlocal total_sum, nested_sum
        for element in nested_list:
            if isinstance(element, int):  # base case: element is an integer
                total_sum *= element
            else:  # recursive case: element is a nested list
                temp = total_sum
                total_sum = 1
                recursive_helper(element)
                nested_sum += total_sum
                total_sum = temp
        return nested_sum
    
    for element in nested_list:
        if isinstance(element, int):  # base case: element is an integer
            total_sum *= element
        else:  # recursive case: element is a nested list
            recursive_helper(element)
    
    return total_sum + nested_sum