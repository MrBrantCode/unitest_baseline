"""
QUESTION:
Write a function `calculate_sum` that takes a list of integers as input and returns the sum of the numbers in the list, excluding any negative numbers, numbers that are divisible by 3, and numbers that contain the digit 5.
"""

def calculate_sum(numbers):
    """
    Calculate the sum of numbers in the list, excluding negative numbers, 
    numbers that are divisible by 3, and numbers that contain the digit 5.
    
    Args:
        numbers (list): A list of integers.
    
    Returns:
        int: The sum of the filtered numbers.
    """
    total_sum = 0
    
    for num in numbers:
        # Exclude negative numbers
        if num < 0:
            continue
        
        # Exclude numbers divisible by 3 or containing the digit 5
        if num % 3 == 0 or '5' in str(num):
            continue
        
        total_sum += num
    
    return total_sum