"""
QUESTION:
Implement a function `find_second_max` that takes an array of numbers as input and returns the second maximum element in the array. The function should not use any built-in sorting functions or methods and should have a time complexity of less than O(n^2). If the array has less than two elements, the function should return None.
"""

def find_second_max(arr):
    if len(arr) < 2:
        return None
    
    max1 = max(arr[0], arr[1])
    max2 = min(arr[0], arr[1])
    
    for i in range(2, len(arr)):
        if arr[i] > max1:
            max2 = max1
            max1 = arr[i]
        elif arr[i] > max2 and arr[i] != max1:
            max2 = arr[i]
    
    return max2