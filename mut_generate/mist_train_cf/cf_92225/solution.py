"""
QUESTION:
Write a function `remove_duplicates(arr)` that takes an array `arr` as input and returns a new array containing the unique elements from `arr`. The function should not use any built-in methods or data structures, such as sets or dictionaries, to store unique values.
"""

def remove_duplicates(arr):
    # Create an empty list to store the unique values
    unique_arr = []

    # Iterate over each element in the input array
    for element in arr:
        # Check if the element is already in the unique array
        if element not in unique_arr:
            # If not, add it to the unique array
            unique_arr.append(element)

    # Return the unique array
    return unique_arr