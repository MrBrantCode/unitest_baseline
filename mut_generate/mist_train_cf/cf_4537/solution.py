"""
QUESTION:
Write a function named `find_max_min_swap` that takes a list of integers as input. The function should swap the positions of the maximum and minimum elements in the list, remove any duplicate elements, sort the list in descending order, and calculate the sum of all elements in the list. The function should return the modified list and the sum of all elements.
"""

def find_max_min_swap(arr):
    # Find the maximum and minimum elements in the array
    max_num = max(arr)
    min_num = min(arr)

    # Swap their positions
    max_index = arr.index(max_num)
    min_index = arr.index(min_num)
    arr[max_index], arr[min_index] = arr[min_index], arr[max_index]

    # Remove duplicates
    arr = list(set(arr))

    # Sort the array in descending order
    arr.sort(reverse=True)

    # Calculate the sum of all elements
    arr_sum = sum(arr)

    return arr, arr_sum