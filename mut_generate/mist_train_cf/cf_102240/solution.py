"""
QUESTION:
Write a function `find_maximum_number` that takes a list of integers as input and returns the maximum number in the list without using any built-in functions or methods. The function should handle the case where the list is empty and return an error message. The time complexity of the function should be O(n), where n is the length of the list, and no additional data structures should be used to store intermediate values.
"""

def findMaximumNumber(nums):
    if len(nums) == 0:
        return "Error: List is empty"

    max_num = float('-inf')
    for num in nums:
        if num > max_num:
            max_num = num

    return max_num