"""
QUESTION:
Develop a function named `dot_product` that takes two 1D arrays (`list1` and `list2`) as input and returns their dot product using recursion. The function should also perform input validation to ensure that `list1` and `list2` are of equal length. The function should not assume any maximum length for the input arrays, but it should note that recursive solutions may cause a stack overflow for very large arrays.
"""

def dot_product(list1, list2, index=0):
    # input validation: check if lists are of same length
    if len(list1) != len(list2):
        return 'Error: lists should have the same length'
    
    # base case: check if we've reached the end of the lists
    if index == len(list1):
        return 0

    # recursive case: calculate the product for the current index and add the result
    # of the recursive call for the next indices
    return list1[index] * list2[index] + dot_product(list1, list2, index+1)