"""
QUESTION:
Write a function `fetch_elements` that takes an array of at least 10 integers and a positive integer `n` as input, and returns the first `n` non-negative elements from the array in ascending order.
"""

def fetch_elements(arr, n):
    # Ensure the array has at least 10 elements
    if len(arr) < 10:
        return "Array should have at least 10 elements"

    # Sort the array in ascending order
    arr.sort()

    # Initialize an empty list to store the fetched elements
    fetched_elements = []

    # Iterate through the sorted array
    for num in arr:
        # Ignore negative elements
        if num < 0:
            continue

        # Add the positive element to the fetched_elements list
        fetched_elements.append(num)

        # Break the loop if we have fetched enough elements
        if len(fetched_elements) == n:
            break

    return fetched_elements