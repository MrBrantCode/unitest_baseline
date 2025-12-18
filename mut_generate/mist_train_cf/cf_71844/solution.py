"""
QUESTION:
Implement the function `complex_math_operations(arr)` that takes an array of integers as input. The function must disregard repeated elements and compute the sum of squares of unique integers along with the sum of distinct integers multiplied by the collective product of signs for each unique number in the array. Signs are noted as 1 for positive, -1 for negative, and 0 for zero. If the array is empty or contains a zero, the function should return None.
"""

def complex_math_operations(arr):
    if len(arr) == 0 or 0 in arr:
        return None
    uniques = {}
    sign_prod = 1
    for num in arr:
        if num < 0:
            uniques[abs(num)] = -1
            sign_prod *= -1
        elif num > 0:
            if abs(num) not in uniques:
                uniques[abs(num)] = 1
    sum_squares = sum([i ** 2 for i in uniques])
    sum_magnitudes = sum([i * uniques[i] * sign_prod for i in uniques])
    return sum_magnitudes, sum_squares