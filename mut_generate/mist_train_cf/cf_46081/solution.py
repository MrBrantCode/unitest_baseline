"""
QUESTION:
Write a function `product_of_elements` that calculates the product of distinct elements in a multi-dimensional list that satisfy a given criterion. The function should ignore duplicate entries and handle empty sub-arrays. The function should take two parameters: `lst` (the multi-dimensional list of integers) and `criterion` (a function that takes an integer and returns a boolean value).
"""

def product_of_elements(lst, criterion):
    """
    Calculate the product of distinct elements in a multi-dimensional list 
    that satisfy a given criterion.

    Parameters:
    lst (list): A multi-dimensional list of integers.
    criterion (function): A function that takes an integer and returns a boolean value.

    Returns:
    int: The product of distinct elements in the list that satisfy the given criterion.
    """
    # Flattening the list and removing duplicate elements
    flattened_list = list(set([num for sublist in lst for num in sublist]))
    
    # Finding the product of the elements which fulfill the criterion
    product = 1
    for num in flattened_list:
        if criterion(num):
            product *= num
    return product