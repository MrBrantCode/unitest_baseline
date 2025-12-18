"""
QUESTION:
Write a function `advanced_math_calc` that takes an array of integers as input. The function should return the product of the signs of the unique integers multiplied by the sum of the absolute values of the unique integers and the product of their squares. If the array contains a '0', return the mean of the unique integers. If the array is empty, return None.
"""

def advanced_math_calc(arr):
    if len(arr) == 0: # Check for empty array
        return None

    unique_set = set(arr) # Remove duplicates by using python's set
    unique_abs_sum = sum(abs(x) for x in unique_set) # sum of absolute values of unique integers

    if 0 in unique_set: # if '0' is present, return mean of unique integer elements
        unique_set.remove(0)
        return unique_abs_sum / len(unique_set) if len(unique_set) > 0 else 0

    unique_square_product = 1 # overall product of squares of unique integers
    sign_product = 1 # joint product of signs corresponding to unique integers
    for num in unique_set:
        unique_square_product *= abs(num)**2
        sign_product *= -1 if num < 0 else 1

    return sign_product * (unique_abs_sum + unique_square_product)