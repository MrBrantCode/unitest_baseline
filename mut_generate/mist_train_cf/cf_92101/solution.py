"""
QUESTION:
Implement the comb_sort function that sorts an input array in ascending order using the Comb Sort algorithm. The function should take a list of integers as input, sort the list in-place, and return the sorted list.
"""

def comb_sort(arr):
    gap = len(arr)
    shrink_factor = 1.3
    sorted = False

    while not sorted:
        gap = int(gap / shrink_factor)
        if gap <= 1:
            gap = 1
            sorted = True

        i = 0
        while i + gap < len(arr):
            if arr[i] > arr[i + gap]:
                arr[i], arr[i + gap] = arr[i + gap], arr[i]
                sorted = False
            i += 1

    return arr