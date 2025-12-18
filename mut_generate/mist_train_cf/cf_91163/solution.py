"""
QUESTION:
Create a function `sort_array` that takes an array of objects and a string key as input, and returns the array sorted by the value of the specified key in descending order. The array will contain at least one object, and each object will have the specified key. The values of the key will always be of the same data type. The function should be case-sensitive when comparing string values.
"""

def sort_array(arr, key):
    return sorted(arr, key=lambda x: x[key], reverse=True)