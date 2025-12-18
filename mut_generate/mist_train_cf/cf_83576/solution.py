"""
QUESTION:
Find the minimum element in a sorted and rotated array that may contain duplicates without using any in-built functions or libraries. The array is of length `n` and is rotated between `1` and `n` times. The function should take an array `nums` as input and return the minimum element.

Restrictions:
- `n == nums.length`
- `1 <= n <= 5000`
- `-5000 <= nums[i] <= 5000`
"""

def find_minimum_element(nums):
    left, right = 0, len(nums) - 1
    while left < right:
        mid = (left + right) // 2
        if nums[mid] > nums[right]:
            left = mid + 1
        elif nums[mid] < nums[right]:
            right = mid
        else: 
            right -= 1   # handle duplicates
    return nums[left]