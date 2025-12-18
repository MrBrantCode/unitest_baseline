"""
QUESTION:
Create a function `max_product_of_three` that takes a list of integers as input and returns the maximum product of any three integers from the list. If the input list contains less than three integers, the function should return None. The input list can contain both positive and negative integers and may contain duplicate integers.
"""

from typing import List, Optional

def max_product_of_three(nums: List[int]) -> Optional[int]:
    if len(nums) < 3:
        return None

    nums.sort()
    return max(nums[-1] * nums[-2] * nums[-3], nums[0] * nums[1] * nums[-1])