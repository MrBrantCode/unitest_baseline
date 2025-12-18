"""
QUESTION:
Create a function called `insertionSort` that takes an array of integers as input and sorts it using the insertion sort algorithm. The function should modify the original array and return the sorted array.
"""

def insertionSort(array):
    # iterate from 1 to length of array
    for i in range(1, len(array)):
        key = array[i]
        j = i - 1
        # shift elements of array[0..i-1], that are greater than key, to one position ahead of their current position
        while j >=0 and key < array[j] :
                array[j + 1] = array[j]
                j -= 1
        array[j + 1] = key
    # return sorted array
    return array