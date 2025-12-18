"""
QUESTION:
Write a function `get_positive` that takes a list of integers as input. The function should sort the list in descending order, filter out the numbers that are less than or equal to 2, and return the filtered list if the sum of its elements is less than or equal to 100. Otherwise, return an empty list.
"""

def get_positive(numbers):
    """
    Function to get positive numbers from a list which are greater than 2 
    and their sum is less than 100
    """
    # Sorting the list in descending order
    numbers.sort(reverse=True)
    
    # List to store the positive numbers > 2
    positive_numbers = [i for i in numbers if i > 2]
    
    # Check if sum exceed 100
    if sum(positive_numbers) > 100:
        # Empty the list and return
        positive_numbers = []
    
    return positive_numbers