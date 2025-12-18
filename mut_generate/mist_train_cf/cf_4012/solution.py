"""
QUESTION:
Create a function named `square_odds` that takes a list of integers as input and returns a tuple containing a list of squared odd numbers and the sum of these squared numbers. The function should skip even numbers and have a time complexity of O(n), where n is the length of the input list.
"""

def square_odds(nums):
    """
    This function takes a list of integers as input, squares the odd numbers, 
    and returns a tuple containing the list of squared odd numbers and their sum.
    
    Args:
    nums (list): A list of integers.
    
    Returns:
    tuple: A tuple containing a list of squared odd numbers and their sum.
    """
    squared_odds = []
    total_sum = 0

    for num in nums:
        if num % 2 != 0:  # Check if number is odd
            squared_num = num ** 2  # Square the number
            squared_odds.append(squared_num)  # Add to the new list
            total_sum += squared_num  # Add to the sum

    return squared_odds, total_sum