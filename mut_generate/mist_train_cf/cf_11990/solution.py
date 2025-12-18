"""
QUESTION:
Implement the `comb_sort` function, which sorts an array using the Comb Sort algorithm. The function should take one parameter, the array to be sorted, and return the sorted array. The Comb Sort algorithm is a modified version of Bubble Sort, with a gap that starts at the length of the array and shrinks by a factor of 1.3 in each iteration until it reaches 1. The array should be sorted in ascending order.
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