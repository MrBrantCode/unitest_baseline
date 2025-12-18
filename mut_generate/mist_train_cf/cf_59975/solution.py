"""
QUESTION:
Implement a function `search(nums, target)` that takes a rotated, ascendingly sorted array `nums` and an integer `target` as input, and returns the index of `target` if it exists in `nums`, or `-1` if it doesn't. The array `nums` is initially sorted in ascending order with unique values and has been rotated at an undisclosed pivot index `k`. The function should have a time complexity of `O(log n)`. Constraints: `1 <= nums.length <= 5000`, `-10^4 <= nums[i] <= 10^4`, and `-10^4 <= target <= 10^4`.
"""

def search(nums, target):
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        if nums[mid] >= nums[left]:
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