"""
QUESTION:
Write a function `find_sublist(numbers, target)` that takes a list of numbers and a target number as input, and returns the smallest sublist whose sum is greater than or equal to the target. If no such sublist exists, return an empty list.
"""

def find_sublist(numbers, target):
    """
    This function takes a list of numbers and a target number as input, 
    and returns the smallest sublist whose sum is greater than or equal to the target.
    
    Args:
        numbers (list): A list of numbers.
        target (int): The target number.
    
    Returns:
        list: The smallest sublist whose sum is greater than or equal to the target.
    """
    window_start = 0
    min_length = float('inf')
    min_sublist = []
    current_sum = 0
    
    for window_end in range(len(numbers)):
        current_sum += numbers[window_end]
        
        while current_sum >= target:
            if window_end - window_start + 1 < min_length:
                min_length = window_end - window_start + 1
                min_sublist = numbers[window_start:window_end + 1]
            current_sum -= numbers[window_start]
            window_start += 1
            
    return min_sublist