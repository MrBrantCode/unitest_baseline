"""
QUESTION:
Write a function called `find_max_num` that takes a list of numbers as input and returns the maximum number in the list. The function should not use built-in functions like `max()` and should iterate through the list starting from the second element to find the maximum number.
"""

def find_max_num(numbers):
    """
    This function finds the maximum number in a given list.
    
    Parameters:
    numbers (list): A list of numbers.
    
    Returns:
    int: The maximum number in the list.
    """
    max_num = numbers[0]
    for num in numbers[1:]:
        if num > max_num:
            max_num = num
    return max_num