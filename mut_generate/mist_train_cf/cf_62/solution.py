"""
QUESTION:
Write a function `generate_histogram(numbers)` that generates a histogram of numbers that are divisible by 3 and greater than 10, displaying their frequency. The histogram should be sorted in descending order based on frequency. The input `numbers` is a list of integers and may contain invalid numbers, but they will be pre-validated to be positive integers between 1 and 1000. The function should return a dictionary where keys are numbers and values are their frequencies. 

Note: The input list `numbers` is pre-validated and contains only integers between 1 and 1000.
"""

def generate_histogram(numbers):
    """
    Generates a histogram of numbers that are divisible by 3 and greater than 10, 
    displaying their frequency. The histogram is sorted in descending order based 
    on frequency.

    Args:
        numbers (list): A list of integers.

    Returns:
        dict: A dictionary where keys are numbers and values are their frequencies.
    """
    histogram = {}
    for number in numbers:
        if number % 3 == 0 and number > 10:
            if number in histogram:
                histogram[number] += 1
            else:
                histogram[number] = 1
    return dict(sorted(histogram.items(), key=lambda x: x[1], reverse=True))