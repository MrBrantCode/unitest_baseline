"""
QUESTION:
Design a function named "check_sorted" that takes a list or matrix as input, verifies if it's sorted or not, and identifies the nature of the sorting (ascending, descending, or lexicographically) if it's sorted. The function should handle lists with different data types (integers, floats, strings) and nested lists, manage exceptions or undefined values, and return a suitable message if the list is not sorted.
"""

def check_sorted(input_list):
    if isinstance(input_list[0], list):
        input_list = [item for sublist in input_list for item in sublist]

    if all(input_list[i] <= input_list[i + 1] for i in range(len(input_list) - 1)):
        return "Ascending"
    elif all(input_list[i] >= input_list[i + 1] for i in range(len(input_list) - 1)):
        return "Descending"
    else:
        return "Not Sorted"