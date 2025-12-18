"""
QUESTION:
Create a function called `reverse_and_square` that takes a list of integers as input, squares each number in the list, and returns the squared numbers in reverse order. The function should work with both positive and negative integers.
"""

def reverse_and_square(nums):
    # Square each number in the list
    squares = [num ** 2 for num in nums]
    # Reverse the list
    reversed_squares = squares[::-1]
    return reversed_squares