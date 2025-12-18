"""
QUESTION:
Create a function named `remove_duplicates` that takes an array as input, removes duplicates, and returns an array of the unique values in descending order. The array can contain integers, floating-point numbers, strings, and nested arrays. The function should use O(1) additional space and have a time complexity of O(n), where n is the length of the input array.
"""

def remove_duplicates(arr):
    # Step 1: Flatten the input array
    def flatten(arr):
        flattened = []
        for val in arr:
            if isinstance(val, list):
                flattened.extend(flatten(val))
            else:
                flattened.append(val)
        return flattened

    # Step 2: Remove duplicates and sort in descending order
    unique_values = sorted(set(flatten(arr)), reverse=True)

    return unique_values