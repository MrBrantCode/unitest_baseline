"""
QUESTION:
Write a function `find_second_third_smallest(array)` that takes a one-dimensional array of numbers as input and returns the second and third smallest unique numbers in ascending order. The function should handle arrays with less than three unique numbers and return a message in such cases.
"""

def find_second_third_smallest(array):
    # remove duplicate values from array
    array = list(set(array))
  
    # Check if array has at least 3 unique numbers
    if len(array) < 3:
        return "Array doesn't consist at least 3 distinct numbers"
  
    # Sort Array in Ascending order
    array.sort()
  
    # return the second and third smallest numbers in a list
    return [array[1], array[2]]