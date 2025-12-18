"""
QUESTION:
Create a function `unique_elements(nums)` that takes a non-empty list of integers as input and returns a list of unique elements from the input list. The function should achieve this in a single pass through the list, with a time complexity of O(n) and a space complexity of O(1), without using any additional data structures or built-in functions that remove duplicates.
"""

def unique_elements(nums):
    j = 0
    for i in range(len(nums)):
        if nums[i] != nums[j]:
            j += 1
            nums[j] = nums[i]
    return nums[:j+1]