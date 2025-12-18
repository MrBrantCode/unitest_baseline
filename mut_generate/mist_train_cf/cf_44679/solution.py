"""
QUESTION:
Implement a function named `insertion_sort` that takes an array of numbers as input and returns the sorted array using the insertion sort technique. The function should be able to handle any size of input array.
"""

def insertion_sort(array):
    # We start from 1 since the first element is trivially sorted
    for index in range(1, len(array)):
        currentValue = array[index]
        position = index
        
        # Move elements of array[0..index-1], that are greater than key,
        # to one position ahead of their current position 
        while position > 0 and array[position - 1] > currentValue:
            array[position] = array[position - 1]
            position -= 1
        array[position] = currentValue
    return array