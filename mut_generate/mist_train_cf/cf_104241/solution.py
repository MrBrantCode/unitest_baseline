"""
QUESTION:
Create a function `calculate_median` that takes a list of numbers as input and returns the median value. The median is the middle value of a sorted list. If the list has an odd number of elements, the median is the middle element. If the list has an even number of elements, the median is the average of the two middle elements.
"""

def calculate_median(numbers):
    """
    Calculate the median of a list of numbers.
    
    Args:
        numbers (list): A list of numbers.
    
    Returns:
        float: The median value of the list.
    """
    sorted_numbers = sorted(numbers)
    
    if len(sorted_numbers) % 2 == 0:
        middle_index = len(sorted_numbers) // 2
        return (sorted_numbers[middle_index] + sorted_numbers[middle_index - 1]) / 2
    else:
        middle_index = len(sorted_numbers) // 2
        return sorted_numbers[middle_index]