"""
QUESTION:
Write a function named `find_second_smallest` that takes one argument, an array of elements. The function should return the second smallest number and its index in the array. If the array has less than two elements, the function should return "Invalid input. At least two elements are required." If the array contains non-numeric data types, the function should return 'Invalid input. Numeric data type expected.' If the array has no second smallest number (all elements are the same), the function should return "No second smallest element in array."
"""

def find_second_smallest(arr):
    if len(arr) < 2:
        return "Invalid input. At least two elements are required."
    smallest = second_smallest = float('inf')
    smallest_index = second_smallest_index = -1
    for i in range(len(arr)):
        if isinstance(arr[i], (int, float)):
            if arr[i] < smallest:
                second_smallest = smallest
                smallest = arr[i]
                second_smallest_index = smallest_index
                smallest_index = i
            elif arr[i] < second_smallest and arr[i] > smallest:
                second_smallest = arr[i]
                second_smallest_index = i
        else:
            return 'Invalid input. Numeric data type expected.'
    if second_smallest == float('inf'):
        return "No second smallest element in array."
    else:
        return second_smallest, second_smallest_index