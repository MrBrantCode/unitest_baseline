"""
QUESTION:
Write a function named `find_max_value` that takes an array of integers as input and returns the maximum value from the array. The function should have a time complexity of O(n) and a space complexity of O(1), where n is the number of elements in the array.
"""

def find_max_value(array):
    max_value = current_max = array[0]
    for i in range(1, len(array)):
        if array[i] > current_max:
            current_max = array[i]
    return current_max