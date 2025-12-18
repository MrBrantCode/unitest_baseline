"""
QUESTION:
Create a function named `sort_array` that takes an array as input, sorts its elements in ascending order, and returns the sorted array. The array contains elements of different data types, including integers and strings. The function should sort the integers in ascending order and place them at the beginning of the array. It should exclude any string elements that contain special characters (such as symbols or numbers) and convert the remaining string elements to lowercase. The string elements should be sorted in ascending order based on their lengths.
"""

import re

def sort_array(arr):
    integers = [element for element in arr if isinstance(element, int)]
    strings = [element.lower() for element in arr if isinstance(element, str) and not re.search('[^a-zA-Z]', element)]
    
    return sorted(integers) + sorted(strings, key=len)