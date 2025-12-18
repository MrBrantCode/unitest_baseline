"""
QUESTION:
Create a function called `combSort` that takes an array of integers as input and returns the sorted array using the Comb Sort algorithm. The Comb Sort algorithm repeatedly swaps adjacent elements if they are in the wrong order, with a decreasing gap size. The gap size starts with the total number of elements in the list and decreases by a factor of 1.3 with each pass until it reaches 1. Implement the Comb Sort algorithm either in-place or by creating a new array for the sorted elements.
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