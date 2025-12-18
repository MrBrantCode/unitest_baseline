"""
QUESTION:
Create a function called `cocktail_shaker_sort(arr)` that sorts a given array of integers using the cocktail shaker sort algorithm. The input array contains at least 1000 elements, and all elements are unique. The function should return the sorted array in ascending order.
"""

def cocktail_shaker_sort(arr):
    n = len(arr)
    start = 0
    end = n - 1
    swapped = True

    while swapped:
        swapped = False

        for i in range(start, end):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True

        if not swapped:
            break

        swapped = False
        end -= 1

        for i in range(end - 1, start - 1, -1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True

        start += 1

    return arr