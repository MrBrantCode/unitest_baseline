"""
QUESTION:
Write a function `perform_operation(nums, k)` that takes in a list of integers `nums` and a string or integer `k`. If `k` is 'rev', reverse the list `nums`. If `k` is an integer, perform the following operations: if `k` is even, remove the element at index `k` from `nums`; if `k` is odd, double the value at index `k` in `nums`. The list `nums` contains 1 to 100 integers in the range [-100, 100]. The function should return the modified list after performing the specified operation.
"""

from typing import List, Union

def entrance(nums: List[int], k: Union[str, int]) -> List[int]:
    if isinstance(k, str) and k == 'rev':
        return list(reversed(nums))
    elif isinstance(k, int):
        if k % 2 == 0:
            del nums[k]
        else:
            nums[k] *= 2
    return nums