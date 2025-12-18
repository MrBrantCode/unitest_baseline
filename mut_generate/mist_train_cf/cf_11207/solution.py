"""
QUESTION:
Create a function `filtered_numbers` that takes a list of integers as input, removes all odd numbers, sorts the remaining even numbers in descending order, and includes only the numbers that are divisible by 3. The function should return the filtered list of integers.
"""

def filtered_numbers(numbers):
    """
    Removes all odd numbers from the input list, sorts the remaining even numbers 
    in descending order, and includes only the numbers that are divisible by 3.
    
    Args:
        numbers (list): A list of integers.
    
    Returns:
        list: The filtered list of integers.
    """
    return sorted(filter(lambda x: x % 2 == 0 and x % 3 == 0, numbers), reverse=True)