"""
QUESTION:
Write a function `weighted_avg` that calculates the weighted average of two arrays of the same length. The function should take two arrays `arr` and `weights` as input, where `arr` contains the numbers and `weights` contains the corresponding weights. The function should return the weighted average as a floating-point number. The function should not use any built-in functions (e.g., no `sum`, `len`, etc.) and should only make a single pass through both arrays.
"""

def weighted_avg(arr, weights):
    total = 0
    weight_sum = 0

    for i in range(0, len(arr)):
        total += arr[i] * weights[i]
        weight_sum += weights[i]
    
    return total / weight_sum