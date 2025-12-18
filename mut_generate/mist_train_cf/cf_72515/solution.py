"""
QUESTION:
Develop a function named `correct_median` that takes an array of numerical data as input and returns its median value. The array may contain integers and floating-point numbers and can be of any size, including an even or odd number of elements, and may contain duplicate values. The function should efficiently handle edge cases and prioritize performance.
"""

def correct_median(array):
    # Sort the array
    array.sort()

    mid = len(array) // 2  

    # if an array has an even number of elements
    if len(array) % 2 == 0:
        median = (array[mid - 1] + array[mid]) / 2.0  
    # if an array has an odd number of elements
    else:
        median = array[mid]

    return median