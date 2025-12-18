"""
QUESTION:
Create a function `is_similarly_oriented` that takes an array of integers as input and returns a boolean value indicating whether all elements in the array are similarly oriented (i.e., either all positive or all negative). The function should handle empty arrays, arrays with one element, and arrays with both positive and negative numbers, as well as zeros. The time complexity of the function should be O(n), where n is the length of the input array.
"""

def is_similarly_oriented(arr):
    if len(arr) < 2:
        return True
    first = arr[0]
    for num in arr:
        if num * first <= 0:
            return False
    return True