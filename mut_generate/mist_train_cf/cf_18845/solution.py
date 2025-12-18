"""
QUESTION:
Write a function `calculate_statistics` that calculates the mean, mode, median, and standard deviation of a given list of numbers. The function should have a time complexity of O(n), not use any built-in statistical libraries or functions, and handle both positive and negative numbers as well as decimal numbers. The function should also handle cases where the input list is empty or contains only a single number, and minimize rounding errors during the calculation of the mean and standard deviation.
"""

def calculate_statistics(numbers):
    """
    This function calculates the mean, mode, median, and standard deviation of a given list of numbers.

    Args:
    numbers (list): A list of numbers.

    Returns:
    tuple: A tuple containing the mean, mode, median, and standard deviation of the input list.
    """
    if not numbers:
        # Handle empty list
        return 0, None, None, 0

    if len(numbers) == 1:
        # Handle list with a single number
        return numbers[0], numbers[0], numbers[0], 0

    n = len(numbers)
    sum_of_numbers = sum(numbers)
    mean = sum_of_numbers / n

    frequency_count = {}
    for num in numbers:
        frequency_count[num] = frequency_count.get(num, 0) + 1

    mode = max(frequency_count, key=frequency_count.get)

    sorted_numbers = sorted(numbers)
    if n % 2 == 1:
        # Calculate median for odd number of elements
        median = sorted_numbers[n // 2]
    else:
        # Calculate median for even number of elements
        mid1 = sorted_numbers[n // 2 - 1]
        mid2 = sorted_numbers[n // 2]
        median = (mid1 + mid2) / 2

    sum_of_squared_diffs = sum((num - mean) ** 2 for num in numbers)
    variance = sum_of_squared_diffs / n
    standard_deviation = variance ** 0.5

    return mean, mode, median, standard_deviation