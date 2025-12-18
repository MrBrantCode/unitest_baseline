"""
QUESTION:
Create a function `divisible_by_3_and_5` that takes a list of integers and returns a new list containing only the elements that are divisible by both 3 and 5, but not by 2. Use list comprehension and lambda functions. The result should be an empty list if there are no such elements.
"""

def divisible_by_3_and_5(numbers):
    """
    Returns a list of integers that are divisible by both 3 and 5, but not by 2.
    
    Args:
        numbers (list): A list of integers.
    
    Returns:
        list: A list of integers that meet the specified conditions.
    """
    return list(filter(lambda x: x % 3 == 0 and x % 5 == 0 and x % 2 != 0, numbers))