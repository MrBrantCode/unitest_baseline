"""
QUESTION:
Write a function `sum_divisible_by_3(arr)` that calculates the sum of elements in the input array `arr` that are divisible by 3, greater than 5, and less than 15.
"""

def sum_divisible_by_3(arr):
    total_sum = 0
    
    for num in arr:
        if num % 3 == 0 and num > 5 and num < 15:
            total_sum += num
    
    return total_sum