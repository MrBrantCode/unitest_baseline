"""
QUESTION:
Create a function named `check_duplicates` that takes one argument, an array of integers, and returns a boolean value. The array must be sorted in ascending order and have a length of 100 or less. If the array contains any negative integers, the function should return False. Otherwise, it should return True if the array contains any duplicate elements and False otherwise.
"""

def check_duplicates(arr):
    # Check length of array
    if len(arr) > 100:
        return False

    # Check for negative integers
    if any(num < 0 for num in arr):
        return False

    # Check for duplicate elements
    for i in range(len(arr)-1):
        if arr[i] == arr[i+1]:
            return True

    return False