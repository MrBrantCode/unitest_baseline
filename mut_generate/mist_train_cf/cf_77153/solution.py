"""
QUESTION:
Design a function named `sum_indexes_median` that takes an array of integers as input and returns the sum of the highest and lowest integers, along with their respective indices (last occurrence in case of duplicates) and the median of the two numbers (rounded to the nearest integer). The function should handle arrays with up to 10^6 elements, as well as up to 10^3 requests, without exceeding time and space complexity constraints. If the input array is empty, the function should return `None`.
"""

def sum_indexes_median(numbers):
    if len(numbers) == 0:
        return None
    highest_number = max(numbers)
    lowest_number = min(numbers)
    highest_index = len(numbers) - 1 - numbers[::-1].index(highest_number)
    lowest_index = len(numbers) - 1 - numbers[::-1].index(lowest_number)
    sum_numbers = highest_number + lowest_number
    median_number = round((highest_number + lowest_number) / 2)
    return sum_numbers, highest_index, lowest_index, median_number