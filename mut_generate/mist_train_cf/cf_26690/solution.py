"""
QUESTION:
Implement a function `max_subarray_sum` that takes a list of integers `arr` as input and returns the maximum sum of any subarray within the given array. The list contains integers in the range -10^4 to 10^4 and has a length between 1 and 10^5. The function should return an integer representing the maximum sum of any subarray.
"""

from typing import List

def max_subarray_sum(arr: List[int]) -> int:
    max_sum = float('-inf')
    current_sum = 0
    
    for num in arr:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)
    
    return max_sum