"""
QUESTION:
Create a function `sort_array(arr, key)` that sorts an array of objects by the value of a certain key in descending order. The key is a string containing a valid Python identifier, and each object in the array has this key. The function should be case-sensitive when comparing string values. The time complexity should not exceed O(n log n) and the space complexity should not exceed O(n).
"""

def sort_array(arr, key):
    return sorted(arr, key=lambda x: x[key], reverse=True)