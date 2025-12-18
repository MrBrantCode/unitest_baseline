"""
QUESTION:
Create a function named `calculate_median` that takes a list of numbers with an odd count as input and returns the median of the numbers without using any built-in functions or libraries.
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