"""
QUESTION:
Write a function `calculate_sum(start, end)` that calculates the sum of all even numbers in the given range from `start` to `end` (inclusive). The function should have a time complexity of O(n), where n is the range of numbers. The function should only use a single loop and no conditional statements. The function should return the sum of even numbers in the given range.
"""

def calculate_sum(start, end):
    """
    Calculate the sum of all even numbers in the given range from start to end (inclusive).
    
    Args:
    start (int): The start of the range (inclusive).
    end (int): The end of the range (inclusive).
    
    Returns:
    int: The sum of even numbers in the given range.
    """
    sum = 0
    if start % 2 != 0:
        start += 1
    for i in range(start, end + 1, 2):
        sum += i
    return sum