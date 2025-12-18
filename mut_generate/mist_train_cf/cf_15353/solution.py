"""
QUESTION:
Write a function named `calculate_median` that takes a list of numbers as input, handles empty lists and non-numeric elements, and returns the median of the numeric elements. The function should work correctly for lists with odd and even numbers of elements and should not assume any specific input format.
"""

def calculate_median(numbers):
    # Check if the list is empty
    if len(numbers) == 0:
        return "Error: The list is empty."

    # Filter out non-numeric elements
    numbers = [num for num in numbers if isinstance(num, (int, float))]

    # Check if the list contains any numeric elements
    if len(numbers) == 0:
        return "Error: The list does not contain any numeric elements."

    # Sort the list in ascending order
    numbers.sort()

    # Calculate the median
    n = len(numbers)
    if n % 2 == 0:
        median = (numbers[n//2 - 1] + numbers[n//2]) / 2
    else:
        median = numbers[n//2]

    return median