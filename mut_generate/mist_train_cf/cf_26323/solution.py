"""
QUESTION:
Write a function named `find_two_largest` that takes a list of integers as input and returns the two largest numbers in the list. The function should assume that the input list contains at least two distinct numbers.
"""

def find_two_largest(numbers):
    """
    This function takes a list of integers as input and returns the two largest numbers in the list.
    
    Parameters:
    numbers (list): A list of integers
    
    Returns:
    tuple: A tuple containing the two largest numbers in the list
    """
    largestOne = max(numbers)
    numbers.remove(largestOne)
    largestTwo = max(numbers)
    
    return largestOne, largestTwo