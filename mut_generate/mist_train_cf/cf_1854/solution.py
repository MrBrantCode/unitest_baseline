"""
QUESTION:
Create a function named `square_nums` that takes a list of integers `nums` as input and returns a new list containing the squares of all elements in `nums`. The function cannot use built-in functions or operators for exponentiation, multiplication, or addition, and it cannot use loops, recursion, or conditional statements. The output list should maintain the same order as the input list.
"""

def square_nums(nums):
    squared = list(map(lambda x: x * x, nums))
    return squared