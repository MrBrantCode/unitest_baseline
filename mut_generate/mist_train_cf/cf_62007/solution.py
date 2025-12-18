"""
QUESTION:
Implement the `bubble_sort` function to sort an array of numbers in ascending order using the Bubble Sort algorithm. The function should accept an array of numbers as input and return the sorted array.
"""

def bubble_sort(arr):
    """
    Sorts an array of numbers in ascending order using the Bubble Sort algorithm.

    Args:
        arr (list): The array of numbers to be sorted.

    Returns:
        list: The sorted array in ascending order.
    """

    # Assign the length of the array to the variable 'len'.
    n = len(arr)

    # The outer loop represents the number of passes the algorithm has to make to ensure the array is sorted.
    for i in range(n):
        # The inner loop represents the comparison and swapping mechanism of the algorithm.
        for j in range(0, n - i - 1):
            # Check if the current element is greater than the next element.
            if arr[j] > arr[j + 1]:
                # Swap the elements if they are in the wrong order.
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    # Return the sorted array.
    return arr