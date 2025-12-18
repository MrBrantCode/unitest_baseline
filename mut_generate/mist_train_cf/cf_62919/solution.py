"""
QUESTION:
Write a function named `prod_signs` that takes a list of integers as input. The function should calculate and return the sum of absolute values of unique non-zero integers and the combined product of their signs in the list. If the list is empty or only contains zeros, return a dictionary indicating that zero and empty arrays are invalid.
"""

def prod_signs(arr):
    """
    Given a list arr of non-zero integers, compute and return the sum of the absolute values of unique integers and the combined product of signs (+1, -1) for each unique number in the list. If the list is empty or only contains zero, return a dictionary indicating that zero and empty arrays are invalid.
    """
    
    unique_arr = list(set(arr))
    if 0 in unique_arr: unique_arr.remove(0)
    
    if not unique_arr: 
        return {'error': 'Invalid input. The list should not contain zeros only or be empty.'}
    else:
        sum_arr = sum(abs(i) for i in unique_arr)
        sign_product = 1
        for i in unique_arr:
            sign_product *= 1 if i > 0 else -1 
        return {'Sum': sum_arr, 'Sign product': sign_product}