"""
QUESTION:
Write a function called `bubbleSort` that takes an unordered list of numbers as input and returns the sorted list. The input list contains only integers and is unsorted. The function should sort the list in ascending order.
"""

def bubbleSort(array):
    for i in range(len(array)):
        for j in range(len(array) - i - 1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
    return array