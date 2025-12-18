"""
QUESTION:
Develop a function named `calculate_disparity` that takes a list of arrays as input and returns a list of tuples. Each tuple should contain the disparity between the maximum and minimum integers within the corresponding array, the indices of the maximum and minimum integers (returning the index of the first occurrence in case of multiple occurrences), and the arithmetic mean of the maximum and minimum integers rounded to the nearest integer. The function should handle empty arrays, duplicate integers, negative integers, and large arrays efficiently without surpassing time and space complexity limitations. The function should be able to process up to 10^6 elements per array and up to 10^3 arrays.
"""

def calculate_disparity(arrays):
    result = []
    for array in arrays:
        if len(array) == 0:
            result.append((0, None, None, None))
            continue

        min_val = min(array)
        max_val = max(array)

        min_index = array.index(min_val)
        max_index = array.index(max_val)

        mean = round((max_val + min_val) / 2)
        disparity = max_val - min_val

        result.append((disparity, max_index, min_index, mean))

    return result