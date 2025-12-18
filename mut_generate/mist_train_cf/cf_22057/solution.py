"""
QUESTION:
Write a function `calculate_statistics` that calculates the average and median of a given list of numbers. The function should take a list of integers as input and return the average and median as output. The average should be calculated as the sum of all numbers divided by the total count of numbers. The median should be calculated as the middle value in the sorted list of numbers. If the list has an even number of elements, the median should be the average of the two middle values.
"""

def calculate_statistics(data):
    """
    Calculate the average and median of a given list of numbers.

    Args:
        data (list): A list of integers.

    Returns:
        tuple: A tuple containing the average and median of the input list.
    """
    average = sum(data) / len(data)
    sorted_data = sorted(data)
    median = (sorted_data[len(sorted_data) // 2 - 1] + sorted_data[len(sorted_data) // 2]) / 2 if len(sorted_data) % 2 == 0 else sorted_data[len(sorted_data) // 2]
    return average, median