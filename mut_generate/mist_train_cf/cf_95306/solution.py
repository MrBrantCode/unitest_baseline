"""
QUESTION:
Write a function `calculate_statistics` that takes an array of positive integers and returns a string representing the mean, median, and mode of the numbers. The function should round the mean to two decimal places and calculate the mode using the highest frequency of occurrence. It should handle duplicate numbers, non-integer inputs, floating-point numbers, and arrays with odd and even lengths, providing error messages when necessary. The time complexity should be O(n) and the space complexity should be O(n).
"""

from collections import Counter
import statistics

def calculate_statistics(arr):
    # Check if the input is valid
    if not isinstance(arr, list) or len(arr) == 0:
        return "Invalid input"

    # Check if all elements are positive integers
    for num in arr:
        if not isinstance(num, int) or num <= 0:
            return "Invalid input"

    # Calculate the mean
    mean = round(sum(arr) / len(arr), 2)

    # Calculate the median
    median = statistics.median(arr)

    # Calculate the mode
    count = Counter(arr)
    max_count = max(count.values())
    mode = [num for num, freq in count.items() if freq == max_count]

    # Return the result as a string
    return f"Mean: {mean}, Median: {median}, Mode: {mode}"