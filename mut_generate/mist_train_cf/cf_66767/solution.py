"""
QUESTION:
Given an array `nums` of integers, implement the function `checkPossibility(nums)` that checks if it could become non-decreasing by modifying at most one element, while ensuring that the modification does not change the parity of the number. The array is considered non-decreasing if `nums[i] <= nums[i + 1]` holds for every `i` where `0 <= i <= n - 2`. Return `True` if it's possible to modify the array, `False` otherwise.

Constraints:
- `n` is the length of the input array `nums`
- `1 <= n <= 10^4`
- `-10^5 <= nums[i] <= 10^5`
"""

def entrance(nums):
    p = None
    for i in range(len(nums) - 1):
        if nums[i] > nums[i+1]:
            if p is not None:
                return False
            p = i

    if p is None or p == 0 or p == len(nums) - 2:
        return True
    elif nums[p-1] <= nums[p+1] or nums[p] <= nums[p+2]:
        if nums[p] % 2 == nums[p+1] % 2 or nums[p-1] % 2 == nums[p+1] % 2:
            return True
    return False