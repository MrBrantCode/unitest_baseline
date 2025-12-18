"""
QUESTION:
Write a function `longest_subarray_less_than_or_equal_to_k` that takes an array `a` and an integer `k` as input, and returns the length of the longest subarray in `a` with a sum less than or equal to `k`. The function should run in O(n) time complexity, where n is the number of elements in the array `a`.
"""

def longest_subarray_less_than_or_equal_to_k(a, k):
    left = 0
    max_length = 0
    current_sum = 0
    
    for right in range(len(a)):
        current_sum += a[right]
        
        while current_sum > k and left <= right:
            current_sum -= a[left]
            left += 1
            
        max_length = max(max_length, right - left + 1)
        
    return max_length