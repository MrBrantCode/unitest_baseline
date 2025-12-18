"""
QUESTION:
Implement the `sort_array` function to sort an array of integers in ascending order without using built-in sorting functions or libraries. The function should have a time complexity of O(n^2) and should be able to handle arrays of any length.

The function should compare each element in the array with every other element and swap positions if the current element is greater than the element being compared. The input array is guaranteed to contain only integers.
"""

def sort_array(arr):
    """
    Sorts an array of integers in ascending order without using built-in sorting functions or libraries.

    Args:
        arr (list): A list of integers to be sorted.

    Returns:
        list: The sorted list of integers.
    """

    # Iterate over the array
    for i in range(len(arr)):
        # Compare each element with every other element
        for j in range(i + 1, len(arr)):
            # Swap positions if the current element is greater than the element being compared
            if arr[i] > arr[j]:
                temp = arr[i]
                arr[i] = arr[j]
                arr[j] = temp

    return arr