"""
QUESTION:
Create a function `sort_array` that takes an array of objects and a key as input, and returns the array sorted by the value of the given key in descending order. The key is a string containing a valid Python identifier. The array has at least one object, and each object has the key specified. The function should be case-sensitive when comparing string values, with a time complexity not exceeding O(n log n) and a space complexity not exceeding O(n).
"""

def sort_array(arr, key):
    return sorted(arr, key=lambda x: x[key], reverse=True)