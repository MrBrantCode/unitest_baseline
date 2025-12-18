"""
QUESTION:
Create a function `calculate_average` that calculates the average of a list of numbers. The function should take a list of numbers as input, calculate the sum of the numbers, and then divide by the total count of numbers. The function should return the calculated average. Ensure the code is optimized for performance and adheres to best practices in coding, including descriptive variable names and proper documentation with comments.
"""

def calculate_average(nums):
    """
    Calculates the average of a list of numbers.

    Args:
        nums (list): A list of numbers.

    Returns:
        The average of the list of numbers.
    """
    total = sum(nums)
    average = total / len(nums)
    return average