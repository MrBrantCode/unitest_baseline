"""
QUESTION:
Design a function called `quick_sort` that sorts a list of pairs of numbers in-place using the QuickSort algorithm. The primary values in each pair should be the main sorting criteria, and the secondary values should be used as tie-breakers when primary values are equivalent. The function should not use Python's built-in sorting methods.
"""

def partition(array, low, high):
    i = low - 1
    pivot = array[high]

    for j in range(low, high):
        # If current value's primary is less than the pivot's primary
        if array[j][0] < pivot[0]:
            i = i + 1
            array[i], array[j] = array[j], array[i]  
        # If primary values are the same, look at secondary values
        elif array[j][0] == pivot[0]:
            if array[j][1] < pivot[1]:
                i = i + 1
                array[i], array[j] = array[j], array[i]  
    
    array[i+1], array[high] = array[high], array[i+1]
    return i + 1

def quick_sort(array, low, high):
    if low < high:
        pi = partition(array, low, high)
        quick_sort(array, low, pi - 1)
        quick_sort(array, pi + 1, high)