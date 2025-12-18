"""
QUESTION:
Create a function `is_sorted` that takes two parameters: an array of integers and a string indicating the order ("ascending" or "descending"). The function should return a boolean indicating whether the array is sorted in the given order. If the order is neither "ascending" nor "descending", the function should return False. The array is considered sorted if it has 0 or 1 elements.
"""

def is_sorted(arr, order):
    if len(arr) <= 1:
        return True
    
    if order != "ascending" and order != "descending":
        return False
    
    if order == "ascending":
        for i in range(1, len(arr)):
            if arr[i] < arr[i-1]:
                return False
    else:
        for i in range(1, len(arr)):
            if arr[i] > arr[i-1]:
                return False
    
    return True