"""
QUESTION:
Given a list of integers `arr`, write a function `max_product` to find the maximum product of any three numbers in the array. The function should consider both positive and negative numbers and have a time complexity of O(n log n) or better. The array will have at least 3 elements and all elements will be within the range of -10^6 to 10^6.
"""

from typing import List

def max_product(arr: List[int]) -> int:
    
    n = len(arr)
    
    # Sort the array
    arr.sort()

    # Get the maximum product
    return max(arr[0] * arr[1] * arr[n - 1], arr[n - 3] * arr[n - 2] * arr[n - 1])