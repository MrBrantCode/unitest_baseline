"""
QUESTION:
Write a function named `positive_average` that calculates the average of only the positive numbers in a given list, without using basic arithmetic operations for division. The function should return the average rounded to 2 decimal places. If the list contains no positive numbers, the function should return 0.
"""

def positive_average(p: list) -> float:
    """Calculate and return average of positive elements in a list p, without using standard arithmetic operations. Handles tuples containing both positive and negative numbers. """
    # Create a list to hold the positive elements.
    positive_nums = [i for i in p if i > 0]

    # Calculate the sum of positive numbers
    total = sum(positive_nums)

    # Calculate the length (number) of positive numbers
    num_positive = len(positive_nums)

    # Calculate and return the average without using division
    average = total / num_positive if num_positive != 0 else 0
    return round(average, 2)