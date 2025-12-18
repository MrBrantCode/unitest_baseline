"""
QUESTION:
Write a function called `find_last_even` that takes a list of integers as input and returns the last even number in the list, or a message indicating that no even number was found. The function should iterate through the list from left to right and only iterate over the list once. If the list is empty or contains no even numbers, the function should return "No even number found."
"""

def find_last_even(numbers):
    """
    This function finds the last even number in a given list of integers.
    
    Args:
        numbers (list): A list of integers.
    
    Returns:
        int: The last even number in the list.
        str: "No even number found" if the list is empty or contains no even numbers.
    """
    even = None
    for num in numbers:
        if num % 2 == 0:
            even = num
    return even if even is not None else "No even number found"