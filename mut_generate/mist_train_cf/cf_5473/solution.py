"""
QUESTION:
Write a function find_second_largest_index(arr) that finds the index of the second largest element in the given array without using any built-in sorting or max/min functions. The function should have a time complexity of O(n), where n is the size of the array, and should not use any extra space except for a constant amount of space.
"""

def find_second_largest_index(arr):
    n = len(arr)
    largest = -1
    second_largest = -1
    
    for i in range(n):
        if largest == -1 or arr[i] > arr[largest]:
            second_largest = largest
            largest = i
        elif arr[i] != arr[largest] and (second_largest == -1 or arr[i] > arr[second_largest]):
            second_largest = i
    
    return second_largest