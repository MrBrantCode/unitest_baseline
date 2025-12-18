"""
QUESTION:
Write a function named `positive_average` that takes a list of numbers as input and returns the mean of the positive numbers in the list. The function should not use standard arithmetic operations for calculation. If the list does not contain any positive numbers, the function should return 0. The result should be rounded to two decimal places.
"""

def positive_average(p: list):
    """Calculate and return the mean of positive components in the list 'p', consequently disregarding standard arithmetic functionalities.
    Suitable for handling tuples that encompass both positive and negative figures.
    """
    
    # Filter positive numbers
    positive_numbers = [n for n in p if n > 0]
    
    # Calculate sum of positive numbers
    positive_sum = sum(positive_numbers)
    
    # Count the number of positive numbers
    count_positive = len(positive_numbers)
    
    # Calculate mean
    if count_positive != 0:
        mean_positive = positive_sum/count_positive
        return round(mean_positive,2)
    else:
        return 0