"""
QUESTION:
Define a function `calculate_median` that takes an array of numbers as its parameter. The array will always have an odd number of elements. Calculate the median without using any built-in functions or libraries. The function should return the median of the array.
"""

def calculate_median(array):
    # Sort the array in ascending order
    for i in range(len(array)):
        for j in range(len(array) - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
    
    # Calculate the index of the middle element
    middle_index = len(array) // 2
    
    # Return the element at the middle index as the median
    return array[middle_index]