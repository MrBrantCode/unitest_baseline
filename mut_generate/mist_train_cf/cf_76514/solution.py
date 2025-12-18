"""
QUESTION:
Create a function `search_in_rotated_sorted_array(nums, target)` that finds an element in a sorted and rotated array. The array is initially sorted in ascending order and then rotated at some unknown pivot. The function should be able to handle duplicate entries and have a time complexity of O(log n). The function should return `True` if the target element is found and `False` otherwise.
"""

def search_in_rotated_sorted_array(nums, target):
    if not nums:
        return False

    left, right = 0, len(nums) - 1

    while left <= right:
        mid = (left + right) // 2

        if nums[mid] == target:
            return True

        # if left part is sorted
        if nums[left] < nums[mid]:
            if nums[left] <= target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        # if right part is sorted
        elif nums[left] > nums[mid]:
            if nums[mid] < target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1
        else:
            # handle duplicates
            left += 1

    return False