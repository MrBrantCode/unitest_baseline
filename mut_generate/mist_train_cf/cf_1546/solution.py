"""
QUESTION:
Write a function `find_greater_elements(arr, num)` that takes an array and a number as input and returns a new array containing elements from the original array that are greater than the given number. The function should have a time complexity of O(n) and must not use built-in functions like filter or map.
"""

def find_greater_elements(arr, num):
    result = []
    for i in range(len(arr)):
        if arr[i] > num:
            result.append(arr[i])
    return result