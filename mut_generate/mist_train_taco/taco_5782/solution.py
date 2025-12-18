"""
QUESTION:
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e.,  [0,1,2,4,5,6,7] might become  [4,5,6,7,0,1,2]).

Find the minimum element.

You may assume no duplicate exists in the array.

Example 1:


Input: [3,4,5,1,2] 
Output: 1


Example 2:


Input: [4,5,6,7,0,1,2]
Output: 0
"""

def find_min_in_rotated_array(nums):
    if len(nums) <= 3:
        return min(nums)
    
    lo = 0
    hi = len(nums) - 1
    mid = (hi + lo) // 2
    
    if nums[mid] < nums[mid - 1] and nums[mid] < nums[mid + 1]:
        return nums[mid]
    
    if nums[mid] > nums[lo] and nums[mid] > nums[hi]:
        return find_min_in_rotated_array(nums[mid:])
    else:
        return find_min_in_rotated_array(nums[:mid + 1])