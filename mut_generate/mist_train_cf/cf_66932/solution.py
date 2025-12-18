"""
QUESTION:
Write a function `find_sqroot(arr, x)` that takes a 2D array `arr` of integers and an integer `x` as input, and returns `True` if the integer square root of `x` exists in `arr`, and `False` otherwise. The array `arr` consists of integers only, and the function should consider only integer square roots of `x`.
"""

def find_sqroot(arr, x):
    # Calculate the integer square root of x
    sqrt_x = int(x**0.5)
    
    # Check if the square of sqrt_x is equal to x to ensure it's an integer square root
    if sqrt_x * sqrt_x == x:
        # Iterate over the array
        for sub_arr in arr:
            if sqrt_x in sub_arr:  # If the integer square root exists in the array, return True
                return True
    return False  # If the integer square root does not exist in the array, return False