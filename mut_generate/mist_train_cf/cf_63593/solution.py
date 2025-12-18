"""
QUESTION:
Write a function `product_list(lst)` that takes a list of numbers as input and returns a new list where each element is the product of all elements of the original list except for the element at the same position. The solution must not use the division operation and must have a linear time complexity.
"""

def product_list(lst):
    n = len(lst)
    
    # Initialize all elements of result list as 1
    res = [1]*n

    # Keep a variable 'left' initialized with 1
    left = 1

    # Calculate the array of left-side products
    for i in range(n):
        res[i] *= left
        left *= lst[i]
    
    # Keep a variable 'right' initialized with 1
    right = 1

    # Calculate the array of right-side products
    for i in range(n-1, -1, -1):
        res[i] *= right
        right *= lst[i]
    
    return res