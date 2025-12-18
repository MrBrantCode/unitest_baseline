"""
QUESTION:
Given an array "a" with "n" elements and a value "k", write a function `longest_subarray_less_than_or_equal_to_k(a, n, k)` that returns the length of the longest subarray in "a" with a sum less than or equal to "k". The function should consider edge cases and have a time complexity of O(n).
"""

def longest_subarray_less_than_or_equal_to_k(a, n, k):
    left = 0
    right = 0
    max_length = 0
    current_sum = 0
    
    while right < n:
        current_sum += a[right]
        right += 1
        
        while current_sum > k:
            current_sum -= a[left]
            left += 1
            
        max_length = max(max_length, right - left)
        
    return max_length