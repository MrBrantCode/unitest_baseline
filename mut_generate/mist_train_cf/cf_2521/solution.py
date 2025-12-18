"""
QUESTION:
Create a function named `check_duplicates` that takes a list of integers as input and returns a boolean value. The input list should be sorted in ascending order and have a length of 100 or less. The function should immediately return False if the list contains any negative integers. Otherwise, it should check for duplicate elements and return True if any are found, and False otherwise. The function should achieve this with a time complexity of O(n) and a space complexity of O(1).
"""

def check_duplicates(arr):
    if len(arr) > 100:
        return False
    if any(num < 0 for num in arr):
        return False
    
    for i in range(len(arr) - 1):
        if arr[i] == arr[i+1]:
            return True
    return False