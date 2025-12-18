"""
QUESTION:
Create a function called `remove_duplicates` that takes a nested array as input. The array can contain integers, floating-point numbers, strings, and nested arrays. The function should remove duplicates from the array, sort the unique values in descending order, and return the result. The function should use O(1) additional space and have a time complexity of O(n), where n is the length of the input array.
"""

def remove_duplicates(arr):
    unique_values = set()
    flattened = []

    def flatten(arr):
        for val in arr:
            if isinstance(val, list):
                flatten(val)
            else:
                unique_values.add(val)

    flatten(arr)
    return sorted(unique_values, reverse=True)