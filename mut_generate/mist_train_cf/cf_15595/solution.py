"""
QUESTION:
Write a function `find_elements(nums)` that takes a list of integers as input and returns a list of integers that appear more than twice in the input list, excluding the number 3. The function should validate the input and return an error message if the input is not a list or if the list contains non-integer elements.
"""

def find_elements(nums):
    if not isinstance(nums, list):
        return "Input must be a list."
    if not all(isinstance(num, int) for num in nums):
        return "All elements in the list must be integers."
    nums = [num for num in nums if num != 3]
    return [num for num in set(nums) if nums.count(num) > 2]