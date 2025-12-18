"""
QUESTION:
Write a function `compute_sum_of_max_digits(arr, K)` that calculates the sum of the maximum K digits in a given array. The function should return -1 if K is greater than the length of the array, and it should consider an array with all non-positive numbers as having a sum of 0. The function should efficiently handle arrays containing negative numbers and zeros.
"""

def compute_sum_of_max_digits(arr, K):
    if K > len(arr):
        return -1
    
    if all(num <= 0 for num in arr):
        return 0
    
    arr.sort()
    max_sum = 0
    num_of_zeros = 0
    
    for num in arr:
        if num == 0:
            num_of_zeros += 1
        elif num < 0:
            break
        else:
            max_sum += num
            K -= 1
            if K == 0:
                break
    
    if num_of_zeros >= K:
        return 0
    
    if K > 0:
        return -1
    
    return max_sum