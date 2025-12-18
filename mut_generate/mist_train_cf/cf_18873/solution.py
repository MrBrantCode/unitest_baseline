"""
QUESTION:
Write a function `product_of_nested_list` that calculates the product of all the elements in a nested list. The function should take a nested list of integers as input, handle cases where the nested list contains empty lists or lists with only one element, and return the product of all the integers in the list. The time complexity of the function should be O(n), where n is the total number of elements in the nested list.
"""

def product_of_nested_list(nested_list):
    # Initialize product to 1
    product = 1

    # Iterate through each element in the nested list
    for element in nested_list:
        # If the element is a list, recursively calculate its product
        if isinstance(element, list):
            sub_product = product_of_nested_list(element)
            # Multiply the product by the sub-product
            product *= sub_product
        # If the element is an integer, multiply the product by the element
        elif isinstance(element, int):
            product *= element

    return product