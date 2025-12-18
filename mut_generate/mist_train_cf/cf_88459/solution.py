"""
QUESTION:
Write a function named `calculate_median` that calculates the median of a given list of numbers with a maximum length of 100, containing duplicate elements, and having both integer and floating-point numbers. The function should have a time complexity of O(nlogn), should not use any built-in libraries or functions to calculate the median, and should return the median with the correct data type.
"""

def calculate_median(data_set):
    # Sort the data set in ascending order
    sorted_data = sorted(data_set)

    # Get the length of the sorted data set
    length = len(sorted_data)

    # Check if the length is even
    if length % 2 == 0:
        # If the length is even, calculate the average of the middle two elements
        middle_right = sorted_data[length // 2]
        middle_left = sorted_data[length // 2 - 1]
        median = (middle_left + middle_right) / 2
    else:
        # If the length is odd, return the middle element
        median = sorted_data[length // 2]

    return median