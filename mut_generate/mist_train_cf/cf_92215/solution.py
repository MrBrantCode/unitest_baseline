"""
QUESTION:
Write a function called `find_min_max_average` that takes a list of numbers as input and returns the minimum, maximum, and average of the numbers without using any built-in functions or methods such as min(), max(), or sum(). The function should handle lists with at least one element.
"""

def find_min_max_average(numbers):
    """
    This function calculates the minimum, maximum, and average of a list of numbers.
    
    Args:
    numbers (list): A list of numbers.
    
    Returns:
    tuple: A tuple containing the minimum, maximum, and average of the input list.
    """
    
    # Initialize variables
    min_num = numbers[0]
    max_num = numbers[0]
    total = 0

    # Find minimum, maximum, and sum
    for num in numbers:
        if num < min_num:
            min_num = num
        if num > max_num:
            max_num = num
        total += num

    # Calculate average
    average = total / len(numbers)

    return min_num, max_num, average