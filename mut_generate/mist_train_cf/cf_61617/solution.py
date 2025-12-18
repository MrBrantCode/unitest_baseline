"""
QUESTION:
Write a function called `product_of_all_elements` that takes a list of integers as input and returns the product of all elements in the list. The function must not use any built-in multiplication function or operator (*) and should have a time complexity of O(n), where 'n' is the number of elements in the list. The function should not use recursion.
"""

def product_of_all_elements(lst):
    """
    This function calculates the product of all elements in a given list.
    
    It does not use any built-in multiplication function or operator (*).
    However, please note that this algorithm has a time complexity of O(n*max(array)) 
    due to repeated addition.

    Args:
        lst (list): A list of integers.

    Returns:
        int: The product of all elements in the list.
    """
    product = 1
    for i in lst:
        counter = 0
        temp = 0
        while counter < abs(i):
            temp += product
            counter += 1
        product = temp if i > 0 else -temp
    return product