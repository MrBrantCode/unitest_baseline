"""
QUESTION:
Write a function `compute_sum_of_max_digits(arr, K)` that calculates the sum of the maximum K digits in a given array `arr`. The array may contain negative numbers and zeros. If K is greater than the length of the array, the function should return -1.
"""

def compute_sum_of_max_digits(arr, K):
    if K > len(arr):
        return -1
    
    sorted_arr = sorted(arr, reverse=True)
    sum_of_max_digits = sum(sorted_arr[:K])
    
    return sum_of_max_digits