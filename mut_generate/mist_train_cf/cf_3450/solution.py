"""
QUESTION:
Create a function named `bubbleSortDescending` that sorts an array of numbers in descending order using the bubble sort algorithm. Implement a flag to indicate whether the array is already sorted before the completion of the sorting algorithm. Ensure the function correctly identifies if the array is already sorted and only returns the sorted array.
"""

def bubbleSortDescending(array):
    for i in range(len(array) - 1):
        flag = True
        for j in range(len(array) - 1 - i):
            if array[j] < array[j + 1]:
                # Swap elements
                array[j], array[j + 1] = array[j + 1], array[j]
                # Update flag
                flag = False
        # If array is already sorted, terminate
        if flag:
            break
    return array