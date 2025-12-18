"""
QUESTION:
Implement the function `get_unique_elements(nums)` that takes a list of integers as input and returns a list of unique elements from the input list. The function should not use any built-in functions or libraries, and it should have a time complexity of O(n^2) and a space complexity of O(1). Assume that the input list is non-empty and contains only integers.
"""

def get_unique_elements(nums):
    unique_elements = []
    for i in range(len(nums)):
        is_unique = True
        for j in range(i + 1, len(nums)):
            if nums[i] == nums[j]:
                is_unique = False
                break
        if is_unique:
            unique_elements.append(nums[i])
    return unique_elements