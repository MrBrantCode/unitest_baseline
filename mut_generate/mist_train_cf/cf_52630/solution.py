"""
QUESTION:
Create a function named 'quicksort' that sorts an array of integers in ascending order. The function should take an array of integers as input and return the sorted array. The solution should have an average and best-case time complexity of O(n log(n)).
"""

def quicksort(array):
    if len(array) <= 1:  # base case
        return array
    pivot = array[len(array) // 2]  
    left = [x for x in array if x < pivot]
    middle = [x for x in array if x == pivot]
    right = [x for x in array if x > pivot]
    return quicksort(left) + middle + quicksort(right)