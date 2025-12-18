"""
QUESTION:
Implement a function named `find_maximum` that takes an array as input. The function should return the maximum integer in the array. If the array is empty or contains non-integer elements, return None. Do not use built-in functions or methods to find the maximum number, and ensure a time complexity of O(n), where n is the length of the array.
"""

def find_maximum(arr):
    if len(arr) == 0:
        return None
    
    max_num = arr[0]
    
    for num in arr:
        if type(num) != int:
            return None
        if num > max_num:
            max_num = num
    
    return max_num