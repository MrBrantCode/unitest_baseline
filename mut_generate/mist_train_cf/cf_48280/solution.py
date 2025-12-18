"""
QUESTION:
Implement a function named 'quicksort' that sorts an array of integers using the quicksort algorithm. The function should take one argument 'array' and return a sorted array. Implement the quicksort algorithm using list comprehensions, and do not use any built-in sorting functions. The function should be able to handle arrays of any size, including empty arrays and arrays with duplicate elements.
"""

def quicksort(array):
    if len(array) <= 1:
        return array
    pivot = array[len(array)//2]
    left = [x for x in array if x < pivot]
    middle = [x for x in array if x == pivot]
    right = [x for x in array if x > pivot]
    return quicksort(left) + middle + quicksort(right)