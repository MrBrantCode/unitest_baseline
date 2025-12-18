"""
QUESTION:
Given a sorted or unsorted array of integers and a target sum, write a function `find_three_numbers(nums, target)` that returns the indices of the three numbers in the array that add up to the target sum. The function should return an empty list if no such triplet exists. The function should be more efficient than a brute-force approach with a time complexity of O(n^3).
"""

def find_three_numbers(nums, target):
    nums.sort()  # Sort the array in ascending order
    n = len(nums)
    for i in range(n - 2):
        left = i + 1  # Pointer to the element next to the current element
        right = n - 1  # Pointer to the last element in the array
        while left < right:
            curr_sum = nums[i] + nums[left] + nums[right]
            if curr_sum == target:
                return [i, left, right]
            elif curr_sum < target:
                left += 1
            else:
                right -= 1
    return []  # If no such triplet exists