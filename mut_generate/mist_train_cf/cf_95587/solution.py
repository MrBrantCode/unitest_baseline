"""
QUESTION:
Implement a function called `combSort` that sorts an array of integers using the Comb Sort algorithm. The function should take an array of integers as input and return the sorted array. The gap size should start with the total number of elements in the list and decrease by a factor of 1.3 with each pass until it reaches 1. The function should repeatedly swap adjacent elements if they are in the wrong order, and it should continue iterating until the gap size is 1 and no more swaps are needed.
"""

def combSort(arr):
    gap = len(arr)
    swapped = True

    while gap > 1 or swapped:
        gap = int(gap / 1.3)
        if gap < 1:
            gap = 1
        swapped = False

        for i in range(len(arr) - gap):
            if arr[i] > arr[i + gap]:
                arr[i], arr[i + gap] = arr[i + gap], arr[i]
                swapped = True

    return arr