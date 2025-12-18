"""
QUESTION:
Find the maximum sum of a subarray in the given array, considering all possible subarrays with a length between 2 and K elements.

Function signature: def max_subarray_sum(array: List[int], K: int) -> int:

Input:
- An array of integers, array (2 <= len(array) <= 10^5)
- An integer, K (2 <= K <= len(array))

Output:
- An integer, the maximum sum of a subarray
"""

from typing import List

def max_subarray_sum(array: List[int], K: int) -> int:
    n = len(array)
    max_sum = float('-inf')  

    for sub_len in range(2, K+1):
        for i in range(n - sub_len + 1):
            sub_sum = sum(array[i:i+sub_len])
            if sub_sum > max_sum:
                max_sum = sub_sum
    
    return max_sum