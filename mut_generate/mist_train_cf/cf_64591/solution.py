"""
QUESTION:
Implement a function `find_closest_elements` that takes an array of integers as input and returns a list of the two closest elements. The input array must contain at least four distinct elements. If the array is empty or contains less than four distinct elements, the function should raise an exception. The function should handle both positive and negative numbers.
"""

def find_closest_elements(input_array):
    if not input_array:
        raise Exception("Input array is empty.")

    distinct_array = set(input_array)
    if len(distinct_array) < 4:
        raise Exception("Input array needs at least four distinct numbers.")

    input_array.sort()

    min_diff = float('inf')
    result = []

    for i in range(len(input_array)-1):
        diff = abs(input_array[i] - input_array[i+1])
        if diff < min_diff:
            min_diff = diff
            result = [input_array[i], input_array[i+1]]

    return result