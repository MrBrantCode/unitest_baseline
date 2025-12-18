"""
QUESTION:
Create a function named `calculate_mean` that takes a list of numbers as input. The function should calculate the mean of the numbers in the list, round it to the nearest integer, and return the result. The input list will contain at least 10 numbers, a maximum of 100 numbers, and the numbers will be in the range of -100 to 100. The list may contain duplicate numbers, which should be handled properly. If the input list is empty, the function should return 0.
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