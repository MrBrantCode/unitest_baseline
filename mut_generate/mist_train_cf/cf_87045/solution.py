"""
QUESTION:
Write a function `calculate_median` that calculates the median of a given list of numbers. The function should handle lists with duplicate numbers, floating-point numbers, and non-numeric values. If the list is empty, the function should return an error message. If there are multiple medians, the function should return both numbers. The function should use an efficient sorting algorithm and handle large lists within a reasonable time limit. The function should be able to handle negative numbers and display the median with the correct sign.
"""

def calculate_median(numbers):
    # Check if the list is empty
    if len(numbers) == 0:
        return "Error: Empty list"

    # Filter out non-numeric values
    numbers = [x for x in numbers if isinstance(x, (int, float))]

    # Sort the list
    numbers.sort()

    # Calculate the median
    n = len(numbers)
    middle = n // 2
    median = None

    if n % 2 == 0:  # Even number of elements
        median = (numbers[middle - 1] + numbers[middle]) / 2
    else:  # Odd number of elements
        median = numbers[middle]

    # Check if there are multiple medians
    if n % 2 == 0 and numbers[middle - 1] != numbers[middle]:
        return f"Multiple medians: {numbers[middle - 1]}, {numbers[middle]}"
    else:
        return median