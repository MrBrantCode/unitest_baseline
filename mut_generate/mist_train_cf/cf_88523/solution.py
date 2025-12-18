"""
QUESTION:
Write a function `find_max_min_swap` that takes an array of integers as input. The function should find the maximum and minimum elements in the array and swap their positions, remove any duplicates from the array, sort the array in descending order, and calculate the sum of all the elements in the array. The function should return the modified array and the sum of its elements.
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