"""
QUESTION:
Create a function `remove_duplicates` that takes an array of integers as input, removes all occurrences of 0 and duplicate elements, and returns the resulting array. The input array can contain both positive and negative integers. You are not allowed to use any built-in functions or data structures other than lists.
"""

def remove_duplicates(arr):
    # Remove all occurrences of 0
    arr = [x for x in arr if x != 0]

    # Initialize an empty list to store unique elements
    unique = []

    # Iterate over the input array
    for num in arr:
        # Check if the current element is already in the unique list
        if num not in unique:
            # If not, append it to the unique list
            unique.append(num)

    # Return the unique list
    return unique