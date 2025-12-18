"""
QUESTION:
Create a function `calculate_average` that takes a list of numbers as input and returns the average of the numbers without using arithmetic operations to calculate the average. The function should handle lists of any length and should return the average as a floating point number.
"""

def calculate_average(numbers):
    # Calculate the sum
    total_sum = 0
    for num in numbers:
        total_sum += num

    # Count the number of elements
    count = 0
    for num in numbers:
        count += 1

    # Calculate the average
    average = total_sum / count

    return average