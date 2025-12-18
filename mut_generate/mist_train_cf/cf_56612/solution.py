"""
QUESTION:
Implement a function `wiggleSort(nums)` that reorders the input array `nums` such that `nums[0] <= nums[1] >= nums[2] <= nums[3]...`. Ensure that adjacent elements are not equal if possible. If it is not possible to avoid equal adjacent elements, return the array as is.

Restrictions: `1 <= nums.length <= 5 * 10^4` and `0 <= nums[i] <= 10^4`. The input array is guaranteed to have a valid answer.
"""

def wiggleSort(nums):
    temp = sorted(nums)
    s = len(temp[::2])
    nums[::2], nums[1::2] = temp[:s][::-1], temp[s:][::-1]
    return nums