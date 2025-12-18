"""
QUESTION:
Write a function `find_max(arr)` that takes an array of integers as input and returns the maximum element in the array. The function should have a time complexity less than O(n log n).
"""

def find_max(arr):
    max_value = arr[0] # Assume first element is the maximum
    for num in arr:
        if num > max_value:
            max_value = num # Update max_value if current element is greater
    return max_value