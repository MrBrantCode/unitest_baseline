"""
QUESTION:
Create a function "foo" that takes a list of integers "nums" as input, removes any duplicate values from the list, and returns a new list containing only the values from the input list that are divisible by 2, in descending order.
"""

def foo(nums):
    """Return a list of even numbers from the input list in descending order, with no duplicates."""
    return sorted([num for num in set(nums) if num % 2 == 0], reverse=True)