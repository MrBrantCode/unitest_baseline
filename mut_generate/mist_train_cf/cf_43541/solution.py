"""
QUESTION:
Create a function named `max_product_list` that takes a collection of lists of numbers (integers and/or floating point numbers) as input. The function should return the list(s) that yield the maximum product when their elements are multiplied together, along with the corresponding maximum product. The function should handle scenarios where the lists contain both positive and negative integers, zero, and floating point numbers. If multiple lists produce the same maximum product, the function should return all such lists. The maximum product should be returned with a precision of 2 decimal places.
"""

def max_product_list(list_of_lists):
    max_product = float('-inf')
    max_lists = []
    
    for lst in list_of_lists:
        product = 1
        for num in lst:
            product *= num
        product = round(product, 2)
        
        if product > max_product:
            max_product = product
            max_lists = [lst]    # start new list
        elif product == max_product:
            max_lists.append(lst)    # add to existing maximum

    return max_lists, max_product