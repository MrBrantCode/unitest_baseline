"""
QUESTION:
Define a function `calculate_nested_list_product(nested_list)` that calculates the sum of the product of the elements of a nested list. The nested list can have up to three levels of nesting, and each element is a positive integer. The function should recursively traverse the nested list, multiply the elements of each sublist, and return the sum of these products.
"""

def calculate_nested_list_product(nested_list):
    """
    This function calculates the sum of the product of the elements of a nested list.
    
    Args:
        nested_list (list): A list of integers or nested lists.
    
    Returns:
        int: The sum of the product of the elements of the nested list.
    """
    
    def calculate_product(sublist):
        product = 1
        for element in sublist:
            if isinstance(element, int):
                product *= element
            else:
                product *= calculate_product(element)
        return product
    
    total_sum = 0
    for element in nested_list:
        if isinstance(element, int):
            total_sum += element
        else:
            total_sum += calculate_product(element)
    
    return total_sum