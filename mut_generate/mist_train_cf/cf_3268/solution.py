"""
QUESTION:
Create a function `same_orientation(arr)` that takes an array of integers or floats as input and returns a boolean value indicating whether all non-zero elements in the array are similarly oriented (i.e., either all positive or all negative). The function should handle arrays with zero, one, or multiple elements, and should have a time complexity of O(n), where n is the length of the input array.
"""

def same_orientation(arr):
    if len(arr) <= 1:
        return True
    elif arr[0] == 0:
        return all(x == 0 for x in arr)
    else:
        orientation = arr[0] > 0
        for num in arr:
            if (num > 0) != orientation:
                return False
        return True