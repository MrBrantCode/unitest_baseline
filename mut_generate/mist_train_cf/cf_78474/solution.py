"""
QUESTION:
Implement the function `can_arrange(arr)` that takes a list of unique integers as input and returns a dictionary with the following information: 

- The largest index of an element not surpassing the preceding one (`'index'`)
- The index of the subsequent smaller element that could be exchanged to potentially rectify the sequence (`'swap_with'`)
- The absolute minimum count of necessary exchanges to correctly arrange the array (`'num_swaps'`)
- The quantity of array inversions (`'inversions'`)

If the input array is already correctly arranged, return `{'index': -1, 'swap_with': -1, 'num_swaps': 0, 'inversions': 0}`.
"""

def can_arrange(arr):
    index = -1
    swap_with = -1
    num_swaps = 0
    inversions = 0

    for i in range(len(arr) - 1):
        if arr[i] > arr[i + 1]:
            swap_with = i + 1
            index = i
            num_swaps += 1
            inversions += 1

        for j in range(i + 2, len(arr)):
            if arr[i] > arr[j]:
                inversions += 1
                if arr[j] < arr[swap_with]:
                    swap_with = j

    return {'index': index, 'swap_with': swap_with, 'num_swaps': num_swaps, 'inversions': inversions}