"""
QUESTION:
Create a function called `get_positive_numbers` that takes a list of numbers as input and returns a new list containing only the positive numbers. The function should have a time complexity of O(n), where n is the length of the input list, and a space complexity of O(n), as the output list's size depends on the input. The function should handle both integers and floating-point numbers.
"""

def entrance(nums):
    result = []
    for num in nums:
        if num > 0:
            result.append(num)
    return result