"""
QUESTION:
Write a function `calculate_sum(nums: List[int], i: int, j: int) -> int` that takes in a list of integers `nums` and two indices `i` and `j`. The function should return the sum of all the elements in the list from index `i` to index `j-1`. If `i` is greater than or equal to `j`, the function should return 0. If `j` is greater than the length of the list, the function should consider the length of the list as the end index.
"""

from typing import List

def calculate_sum(nums: List[int], i: int, j: int) -> int:
    """
    This function calculates the sum of elements in a list from index i to j-1.
    
    Args:
    nums (List[int]): A list of integers.
    i (int): The start index.
    j (int): The end index.
    
    Returns:
    int: The sum of elements in the list from index i to j-1.
    """
    
    if i >= j:
        return 0
    if j > len(nums):
        j = len(nums)

    return sum(nums[i:j])