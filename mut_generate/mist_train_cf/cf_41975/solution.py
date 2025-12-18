"""
QUESTION:
Write a function `max_product_of_three` that takes in a list of integers and returns the maximum product of any three numbers in the list. If the input list contains less than three integers, the function should return None. The function should handle both positive and negative integers, and consider that the maximum product can be either the product of the three largest numbers or the product of the two smallest (most negative) numbers and the largest number.
"""

from typing import List, Optional

def max_product_of_three(nums: List[int]) -> Optional[int]:
    if len(nums) < 3:
        return None
    
    nums.sort()
    return max(nums[-1] * nums[-2] * nums[-3], nums[0] * nums[1] * nums[-1])