"""
QUESTION:
Develop a function named `multiply_tuple_elements` that takes two parameters: a tuple `tup` and a list `result_list`. The function should multiply all elements in the tuple, including elements within any nested tuples, and append the result to `result_list`. If the result already exists in `result_list`, the function should increment the result by 1 until it is unique before appending.
"""

def multiply_tuple_elements(tup, result_list):
    product = 1
    for i in tup:
        if isinstance(i, tuple):
            product *= multiply_tuple_elements(i, result_list)
        else:
            product *= i

    # Check if the product is already in the list
    while product in result_list:
        product += 1
    result_list.append(product)
    
    return product