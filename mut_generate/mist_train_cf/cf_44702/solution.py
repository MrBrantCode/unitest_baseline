"""
QUESTION:
Write a function `findSmallest(arr)` that takes an unsorted array of numbers as input and returns the smallest number in the array. The function should have a time complexity of O(n) and a space complexity of O(1), where n is the size of the array. Assume the input array is not empty.
"""

def findSmallest(arr):
    smallest = arr[0]
    for i in arr:
        if i < smallest:
            smallest = i
    return smallest