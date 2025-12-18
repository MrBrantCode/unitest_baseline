"""
QUESTION:
Implement the function `removeDuplicates(nums)` which removes duplicates from a sorted array `nums` in-place, maintaining the order of the remaining elements, and returns the new length of the array. 

The function should have the following properties: 

- The order of the remaining elements after removing duplicates should be the same as their original order in the array.
- The function should modify the input array in-place with O(1) extra memory.
- The input array `nums` is sorted in ascending order.
- The length of `nums` is between 0 and 3 * 10^4 (inclusive), and each element in `nums` is between -10^4 and 10^4 (inclusive).
"""

def removeDuplicates(nums):
    if len(nums) == 0:
        return 0
    i = 0
    for j in range(1, len(nums)):
        if nums[j] != nums[i]:
            i += 1
            nums[i] = nums[j]
    return i + 1