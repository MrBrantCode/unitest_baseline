"""
QUESTION:
Write a function named `product_of_nested_list` that calculates the product of all elements in a nested list containing integers and sublists of integers. The function should handle nested lists of varying lengths, including empty lists, and have a time complexity of O(n), where n is the total number of elements in the nested list.
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