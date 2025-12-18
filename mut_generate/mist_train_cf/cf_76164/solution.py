"""
QUESTION:
Implement a function named `bubble_sort` that manually sorts an array of integers into ascending numerical order without using any built-in sorting functions. Additionally, implement a function named `validate_sorting` that verifies if the array is sorted in ascending order, returning `True` if the array is sorted correctly and `False` otherwise.
"""

def bubble_sort(array):
    n = len(array)
    
    for i in range(n):
        for j in range(0, n-i-1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
                
    return array


def validate_sorting(array):
    n = len(array)
    
    for i in range(n-1):
        if array[i] > array[i+1]:
            return False
            
    return True