"""
QUESTION:
Write a function named `calculate_statistics` that calculates the maximum, minimum, and median of a list of numbers. The function should handle lists with duplicates and negative numbers. It should also exclude outliers (the top and bottom 25% of the data) when calculating the median. If the list is empty, the function should return `None` for all statistics. If the list contains only one element, the function should return that element as the minimum, maximum, and median.
"""

def calculate_statistics(numbers):
    if len(numbers) == 0:
        return None, None, None

    minimum = min(numbers)
    maximum = max(numbers)

    # Exclude outliers when calculating the median
    sorted_numbers = sorted(numbers)
    outliers = len(sorted_numbers) // 4  # Exclude top and bottom 25% of the data

    median = None
    if outliers > 0 and len(numbers) > 2:
        sorted_numbers = sorted_numbers[outliers:-outliers]
        if len(sorted_numbers) % 2 == 0:
            median = (sorted_numbers[len(sorted_numbers) // 2 - 1] + sorted_numbers[len(sorted_numbers) // 2]) / 2
        else:
            median = sorted_numbers[len(sorted_numbers) // 2]

    return minimum, maximum, median