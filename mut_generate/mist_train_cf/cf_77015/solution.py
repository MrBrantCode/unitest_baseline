"""
QUESTION:
Write a function get_product_array that takes an array of integers as input and returns an array of the same size where each element is the product of all the elements in the original array except itself. The solution should not use division and should operate in O(n) time complexity.
"""

def get_product_array(lst):
    # Initialize a variable to keep track of the product
    right_product = 1
    # Initialize an array of ones with the same size as the input
    output = [1] * len(lst)
    
    # Calculate the product of the numbers before the current index
    for i in range(1, len(lst)):
        output[i] = output[i - 1] * lst[i - 1]
   
    # Calculate the product of the numbers after the current index
    for i in range(len(lst) - 1, -1, -1):
        output[i] *= right_product
        right_product *= lst[i]
    
    return output