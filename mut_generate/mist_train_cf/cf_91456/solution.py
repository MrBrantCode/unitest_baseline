"""
QUESTION:
Create a function named `check_consecutive_elements` that takes an array and a value as input. The function should return True if any two consecutive elements in the array are equal to the given value, and False otherwise.
"""

def check_consecutive_elements(arr, value):
    for i in range(len(arr) - 1):
        if arr[i] == value and arr[i+1] == value:
            return True
    return False