"""
QUESTION:
Write a function `get_positive_numbers(nums)` that takes a list of numbers as input and returns a new list containing only the positive numbers. The function should have a time complexity of O(n), where n is the length of the input list, and a space complexity of O(n), as the output list size depends on the input list size.
"""

def get_positive_numbers(nums):
    result = []
    for num in nums:
        if num > 0:
            result.append(num)
    return result