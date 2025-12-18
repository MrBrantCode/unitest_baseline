"""
QUESTION:
Implement a function `cocktailSort(arr)` that sorts an input array `arr` using the Two-way bubble sort (or Cocktail sort) algorithm. The function should iterate through the array from both ends, swapping adjacent elements that are out of order. If no swaps are made during a full pass, the function should stop prematurely. The function should also handle edge cases, such as an empty array or an array with only one element, and return the sorted array.
"""

def cocktailSort(arr):
    n = len(arr)
    swapped = True
    start = 0
    end = n - 1
    while (swapped == True):

        swapped = False

        for i in range(start, end):
            if (arr[i] > arr[i + 1]) :
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True

        if (swapped == False):
            break

        swapped = False
        end = end - 1

        for i in range(end - 1, start - 1, -1):
            if (arr[i] > arr[i + 1]):
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True

        start = start + 1

    return arr