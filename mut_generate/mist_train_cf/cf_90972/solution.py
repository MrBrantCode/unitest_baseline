"""
QUESTION:
Create a function named `find_max` that takes an array as input and returns the maximum number in the array without using the built-in max() function. The solution must have a time complexity of O(n), where n is the number of elements in the array. The array contains at least one element.
"""

def find_max(array):
    max_number = array[0]
    
    for i in range(1, len(array)):
        if array[i] > max_number:
            max_number = array[i]
    
    return max_number