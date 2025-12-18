"""
QUESTION:
Write a function `find_smallest(arr)` that finds the smallest number in an array of numbers without using any built-in functions or methods. The function should have a time complexity of O(n), handle negative numbers, duplicate numbers, and large arrays efficiently, and should not modify the original array.
"""

def find_smallest(arr):
    smallest = arr[0]
    
    for num in arr[1:]:
        if num < smallest:
            smallest = num
    
    return smallest