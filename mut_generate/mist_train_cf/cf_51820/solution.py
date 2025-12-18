"""
QUESTION:
Create a function named `insertionSort` that sorts an array of integers in ascending order using the insertion sort algorithm. The function should take one parameter, `arr`, which is the input array to be sorted. The function should return the sorted array. The function should not use any built-in sorting functions and should only use a single loop and a while loop to shift elements.
"""

def insertionSort(arr):
    # Go through 1 to len(arr)
    for i in range(1, len(arr)):
        key = arr[i]
        # Move elements of arr[0..i-1], that are greater than key,
        # to one position ahead of their current position
        j = i-1
        while j >= 0 and key < arr[j] :
                arr[j + 1] = arr[j]
                j -= 1
        arr[j + 1] = key
    return arr