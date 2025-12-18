"""
QUESTION:
Create a function called `calculate_average` that computes the average of a list of numbers, excluding any numbers that are divisible by 5.
"""

def calculate_average(numbers):
    """
    Computes the average of a list of numbers, excluding any numbers that are divisible by 5.

    Args:
    numbers (list): A list of numbers.

    Returns:
    float: The average of the numbers that are not divisible by 5.
    """
    # Filter out numbers that are divisible by 5
    filtered_numbers = [num for num in numbers if num % 5 != 0]
    
    # Check if there are any numbers left after filtering
    if len(filtered_numbers) == 0:
        return 0
    
    # Calculate the sum of the remaining numbers
    total = sum(filtered_numbers)
    
    # Calculate the average
    average = total / len(filtered_numbers)
    
    return average