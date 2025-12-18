"""
QUESTION:
Design a function called `adjust_sequence` that takes an array of unique integers as input and returns a dictionary containing the largest index of an element which is not greater than or equal to the element before it, the index of the subsequent smaller element that can be swapped with it to potentially correct the sequence, and the cumulative count of necessary swaps. If no such element exists, return {'index': -1, 'swap_with': -1, 'total_swaps': 0}.
"""

def adjust_sequence(arr):
    total_swaps = 0
    swapped = True
    result = {'index': -1, 'swap_with': -1, 'total_swaps': 0}

    while swapped:
        swapped = False
        i = 0
        while i < len(arr)-1:
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                total_swaps += 1
                swapped = True
                result = {'index': i+1, 'swap_with': i, 'total_swaps': total_swaps}
            i += 1
    return result