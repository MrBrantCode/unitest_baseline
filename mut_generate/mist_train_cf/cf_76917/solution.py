"""
QUESTION:
Write a function named `sum_elements` that takes an array of elements as input, calculates the sum of all integer elements, and reports any non-integer elements along with their positions in the array. The function should ignore non-integer entries and return the sum of integers and a list of error reports. The array positions in the error report should be 1-indexed.
"""

def sum_elements(array):
    total_sum = 0
    error_report = []
    for i in range(len(array)):
        if isinstance(array[i], int):
            total_sum += array[i]
        else:
            error_report.append(f"Non-integer entry '{array[i]}' found at position {i+1}")
    return total_sum, error_report