"""
QUESTION:
Implement a function `cocktail_shaker_sort(arr)` that sorts the elements of the input array `arr` in ascending order using the cocktail shaker sort methodology. The function should return the sorted array. The input array will contain integers, and the function should modify the original array in-place.
"""

def cocktail_shaker_sort(arr):
    n = len(arr)
    swapped = True
    start = 0
    end = n-1

    while (swapped == True):
        swapped = False

        for i in range (start, end):
            if (arr[i] > arr[i + 1]) :
                arr[i], arr[i + 1]= arr[i + 1], arr[i]
                swapped = True

        if (swapped == False):
            break

        swapped = False

        end = end-1

        for i in range(end-1, start-1, -1):
            if (arr[i] > arr[i + 1]):
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True

        start = start+1

    return arr