"""
QUESTION:
Write a function `cumulative_unique_count` that takes a multidimensional array (up to 3 levels deep) as input and returns the cumulative count of unique constituents.
"""

def cumulative_unique_count(array):
    def flatten(array):
        result = []
        for i in array:
            if isinstance(i, list):
                result += flatten(i)
            else:
                result.append(i)
        return result

    flattened_array = flatten(array)
    unique_elements = set(flattened_array)
    return len(unique_elements)