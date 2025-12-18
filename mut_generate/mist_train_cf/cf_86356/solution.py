"""
QUESTION:
Write a function `find_second_smallest` that takes a list of integers as input. The list contains at least 10 unique integers in the range -10000 to 10000. The function should return the second smallest integer in the list.
"""

def find_second_smallest(numbers):
    """
    This function finds the second smallest integer in a list of integers.
    
    Parameters:
    numbers (list): A list of integers containing at least 10 unique integers in the range -10000 to 10000.
    
    Returns:
    int: The second smallest integer in the list.
    """
    smallest = float('inf')
    second_smallest = float('inf')
    for num in numbers:
        if num < smallest:
            second_smallest = smallest
            smallest = num
        elif num < second_smallest and num != smallest:
            second_smallest = num
    return second_smallest