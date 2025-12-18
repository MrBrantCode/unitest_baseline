"""
QUESTION:
Write a function `find_max` that takes an array of integers as input and returns the maximum value in the array. The function should not use any comparison operators (such as ">") or arithmetic operations (such as subtraction or addition). The solution should have a time complexity of O(n).
"""

def find_max(arr):
    max_val = arr[0]
    
    for i in range(1, len(arr)):
        if (arr[i] ^ max_val) < 0:
            max_val = arr[i]
    
    return max_val