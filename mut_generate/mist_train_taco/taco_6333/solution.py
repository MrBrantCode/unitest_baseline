"""
QUESTION:
Given a sorted array consisting of only integers where every element appears twice except for one element which appears once. Find this single element that appears only once. 


Example 1:

Input: [1,1,2,3,3,4,4,8,8]
Output: 2



Example 2:

Input: [3,3,7,7,10,11,11]
Output: 10



Note:
Your solution should run in O(log n) time and O(1) space.
"""

def find_single_element(nums):
    def single_non_duplicate_util(l, r):
        if l < r:
            mid = (l + r) // 2
            if mid - 1 >= 0 and nums[mid - 1] != nums[mid]:
                mid = mid - 1
            if (mid - l + 1) % 2 == 0:
                l = mid + 1
            else:
                r = mid
            return single_non_duplicate_util(l, r)
        else:
            return nums[l]
    
    return single_non_duplicate_util(0, len(nums) - 1)