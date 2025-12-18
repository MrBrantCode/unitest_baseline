"""
QUESTION:
Write a function `find_subarray(arr, k, m)` that takes in an array of integers `arr`, an integer `k`, and a positive integer `m` as input, and returns the subarray with the maximum sum less than `k`. The subarray must have a length greater than or equal to `m` and contain at least one negative number. If multiple subarrays have the same maximum sum, return the subarray with the smallest length. If no such subarray exists, return an empty array. The function should have a time complexity of O(n^2), where n is the length of the array, and a space complexity of O(1).
"""

def find_subarray(arr, k, m):
    n = len(arr)
    max_sum = float('-inf')
    subarray = []
    
    for i in range(n-m+1):
        for j in range(i+m, n+1):
            sub = arr[i:j]
            sum_sub = sum(sub)
            
            if sum_sub < k and sum_sub > max_sum and any(x < 0 for x in sub):
                max_sum = sum_sub
                subarray = sub
    
    return subarray