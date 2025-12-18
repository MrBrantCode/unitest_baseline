"""
QUESTION:
Write a function named `find_most_frequent` that finds the most frequent item in an array of integers, with the following constraints:

- The function should have a time complexity of O(n log n), where n is the length of the array.
- The function should not use any built-in sorting or counting functions/methods.
- The function should use constant space complexity, i.e., it should not use any additional data structures apart from a small constant amount of variables.

The function should return the most frequent item in the array. If multiple items have the same maximum frequency, the function can return any one of them.
"""

def find_most_frequent(arr):
    # Sort the array using quicksort
    def quicksort(arr, low, high):
        if low < high:
            pivot_index = partition(arr, low, high)
            quicksort(arr, low, pivot_index - 1)
            quicksort(arr, pivot_index + 1, high)

    def partition(arr, low, high):
        pivot = arr[high]
        i = low - 1
        for j in range(low, high):
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1

    quicksort(arr, 0, len(arr) - 1)

    # Initialize variables
    max_count = 0
    max_item = None
    count = 1
    item = arr[0]

    # Iterate through the sorted array
    for i in range(1, len(arr)):
        if arr[i] == item:
            count += 1
        else:
            if count > max_count:
                max_count = count
                max_item = item
            count = 1
            item = arr[i]

    # Compare count with max_count one last time
    if count > max_count:
        max_count = count
        max_item = item

    # Return the most frequent item
    return max_item