"""
QUESTION:
Create a function named calculate_median that takes a list of elements as input. The function should return the median of the numeric values in the input list, rounded to the nearest integer. If the input list is empty or contains no numeric values, the function should return None. The function should have a time complexity of O(n log n) and a space complexity of O(n), where n is the length of the input list.
"""

def calculate_median(input_list):
    if len(input_list) == 0:
        return None

    numeric_list = [x for x in input_list if isinstance(x, (int, float))]
    if len(numeric_list) == 0:
        return None

    sorted_list = sorted(numeric_list)
    mid_index = len(sorted_list) // 2

    if len(sorted_list) % 2 == 0:
        median = (sorted_list[mid_index - 1] + sorted_list[mid_index]) / 2
    else:
        median = sorted_list[mid_index]

    return round(median)