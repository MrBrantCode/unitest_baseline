"""
QUESTION:
Write a function named `swap_if_even` that takes a list of unique integers and two indices as input. The function should swap the elements at these indices if their sum is even and return the modified list. If the sum is not even, it should return the original list. The function should handle exceptions due to improper indices (out of bounds, negative) and return an error message instead.
"""

def swap_if_even(arr, i, j):
    try:
        # Verify if sum is even
        if (arr[i] + arr[j]) % 2 == 0:
            # Swap elements
            arr[i], arr[j] = arr[j], arr[i]
    except IndexError: 
        # return a message for improper indices
        return ("One of the indices is out of bounds of the list")
    return arr