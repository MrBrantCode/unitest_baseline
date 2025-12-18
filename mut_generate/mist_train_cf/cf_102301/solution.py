"""
QUESTION:
Create a function named `calculate_mean` that takes a list of integers as input and returns the rounded mean of the numbers in the list. The input list will contain at least 10 and at most 100 numbers in the range of -100 to 100. The function should handle duplicate numbers in the list.
"""

def calculate_mean(numbers):
    # Check if the input list is empty
    if len(numbers) == 0:
        return 0

    # Calculate the sum of all numbers in the list
    total_sum = sum(numbers)

    # Calculate the mean by dividing the sum by the total number of elements
    mean = total_sum / len(numbers)

    # Round the mean to the nearest integer
    rounded_mean = round(mean)

    return rounded_mean