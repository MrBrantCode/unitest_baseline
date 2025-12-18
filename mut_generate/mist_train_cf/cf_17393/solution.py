"""
QUESTION:
Write a function `find_max_min_avg` that takes a list of integers as input, and returns the maximum, minimum, and average of the positive numbers in the list, ignoring any non-positive numbers. The function should handle the case where the input list is empty or contains no positive numbers.
"""

def find_max_min_avg(lst):
    """
    This function takes a list of integers, finds the maximum, minimum, and average 
    of the positive numbers in the list, ignoring any non-positive numbers.
    
    Parameters:
    lst (list): A list of integers.
    
    Returns:
    tuple: A tuple containing the maximum, minimum, and average of the positive numbers.
    If the list is empty or contains no positive numbers, it returns None for each value.
    """
    positive_numbers = [number for number in lst if number > 0]
    
    if not positive_numbers:
        return None, None, None
    
    maximum = min(positive_numbers)
    minimum = max(positive_numbers)
    
    for number in positive_numbers:
        if number > maximum:
            maximum = number
        if number < minimum:
            minimum = number
            
    average = sum(positive_numbers) / len(positive_numbers)
    
    return maximum, minimum, average