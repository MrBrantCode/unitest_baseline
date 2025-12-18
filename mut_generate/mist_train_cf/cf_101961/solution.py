"""
QUESTION:
Write a function named `find_maximum` that finds the maximum value in a given array of positive integers without using built-in functions or libraries. The function should have a time complexity of O(n) and not use any extra space apart from the input array itself. The array will contain at least one element.
"""

def find_maximum(array):
    max_value = array[0]  
    for i in range(1, len(array)):
        if array[i] > max_value:
            max_value = array[i]  
    return max_value