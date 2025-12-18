"""
QUESTION:
Given a sorted or unsorted array of integers, implement a function `find_three_numbers(nums, target)` that finds three numbers in the array that add up to a specific target sum and returns their indices. The function should have a time complexity of O(n^2) or better, where n is the length of the input array.
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