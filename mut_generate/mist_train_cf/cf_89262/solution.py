"""
QUESTION:
Write a function `find_maximum(arr)` that takes an array of elements as input and returns the maximum integer in the array. If the array is empty or contains non-integer elements, the function should return `None`. The function must not use any built-in functions or methods to find the maximum number, and it must have a time complexity of O(n), where n is the length of the array.
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