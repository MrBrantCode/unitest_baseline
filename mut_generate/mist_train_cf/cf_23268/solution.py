"""
QUESTION:
Write a function `longest_element` that takes a list of integers as input and returns the integer with the most digits. The function should return the first integer with the maximum number of digits in case of a tie.
"""

def longest_element(nums):
    max_length = 0
    max_length_item = None

    for num in nums:
        if len(str(num)) > max_length:
            max_length = len(str(num))
            max_length_item = num

    return max_length_item