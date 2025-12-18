"""
QUESTION:
Given a rotated sorted array `nums` that may contain duplicates and an integer `target`, write a function `search(nums, target)` that returns the index of `target` if it exists in `nums`, or -1 if it does not. The array `nums` has a length between 1 and 5000, inclusive, and its elements are integers between -10^4 and 10^4, inclusive. The `target` is also an integer between -10^4 and 10^4, inclusive.
"""

def search(nums, target):
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = left + (right - left) // 2

        if nums[mid] == target:
            return mid  

        while left < mid and nums[left] == nums[mid]:  
            left += 1

        if nums[left] <= nums[mid]:  
            if nums[left] <= target < nums[mid]:  
                right = mid - 1
            else:  
                left = mid + 1
        else:  
            if nums[mid] < target <= nums[right]:  
                left = mid + 1
            else:  
                right = mid - 1

    return -1  