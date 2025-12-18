"""
QUESTION:
Create a function named `complex_math_operations` that takes a list of integers as input. The function should ignore zero and repeated entries, calculate the sum of squares of unique integers, and calculate the sum of absolute values of unique integers multiplied by the product of signs for every unique number in the list. Signs are represented as 1 for positive, -1 for negative, and 0 for zero. If the input list is empty, the function should return None.
"""

def complex_math_operations(arr):
    arr = [e for e in arr if e] # filter out 0s
    if not arr: # if empty list
        return None

    unique_nums = set(arr)
    sum_of_squares = sum(num**2 for num in unique_nums)
    product_of_signs = 1

    for num in arr:
        if num < 0:
            product_of_signs *= -1
        elif num > 0:
            product_of_signs *= 1

    sum_of_magnitudes = sum(abs(num) for num in unique_nums) * product_of_signs

    return sum_of_squares, sum_of_magnitudes