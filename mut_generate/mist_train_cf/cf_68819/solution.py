"""
QUESTION:
Create a function named `smallest_disparity` that takes a list of elements as input, identifies the pair of elements with the smallest disparity, and returns the disparity along with the pair of elements. The input list can contain integers, floating-point numbers, and non-numeric elements. If the list contains less than two numeric elements, return a suitable error message. Ignore non-numeric elements during the calculation.
"""

def smallest_disparity(array):
    numeric_array = [i for i in array if isinstance(i, (int, float))]

    if len(numeric_array) < 2:
        return "Array should contain at least two numeric elements"

    numeric_array.sort()
    min_difference = float('inf')
    result = ()
    
    for i in range(1, len(numeric_array)):
        difference = abs(numeric_array[i] - numeric_array[i-1])
        if difference < min_difference:
            min_difference = difference
            result = (numeric_array[i-1], numeric_array[i])

    return min_difference, result