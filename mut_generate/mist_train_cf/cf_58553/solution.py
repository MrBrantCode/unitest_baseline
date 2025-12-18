"""
QUESTION:
Create a function `is_even_sum(nums)` that checks if there is at least one even number in a non-empty list of integers. The function should use a recursive approach and return `True` if an even number is found, and `False` otherwise. Restrict the use of Python built-in functions such as `sum()` and do not use explicit loops (for, while). The solution should utilize functional programming concepts and recursion only.
"""

def entance(nums):
    if len(nums)==0:          # Base Case: If list is empty
        return False
    elif nums[0] % 2 == 0:    # If first number is even
        return True
    else:                     # If first number is not even, call the function for the tail of the list
        return entance(nums[1:])