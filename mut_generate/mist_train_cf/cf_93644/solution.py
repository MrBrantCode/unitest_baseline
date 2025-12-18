"""
QUESTION:
Write a function `find_maximum(arr)` that finds the maximum value in the given array of positive integers without using any built-in functions or libraries. The function should have a time complexity of O(n) and should not use any extra space apart from the given array itself.
"""

def find_maximum(arr):
    max_value = arr[0]  
    for num in arr:
        if num > max_value:
            max_value = num
    return max_value