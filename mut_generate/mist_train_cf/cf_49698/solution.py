"""
QUESTION:
Write a function named `can_arrange` that takes a list of integers without repeated values as input. The function should return a dictionary containing the largest index of an element that is not in its correct position in the sorted array (or -1 if no such element exists), the index of the subsequent smaller element that can be swapped with it to possibly correct the sequence (or -1 if no swap is needed), and the total number of swaps needed to correct the sequence.
"""

def can_arrange(arr):
    largest_idx = -1
    swap_idx = -1
    total_swaps = 0

    for i in range(1, len(arr)):
        if arr[i] < arr[i - 1]:
            j = i
            while j > 0 and arr[j] < arr[j - 1]:
                arr[j], arr[j - 1] = arr[j - 1], arr[j]
                largest_idx = j - 1
                swap_idx = j
                total_swaps += 1
                j -= 1

    return {"index": largest_idx, "swap_with": swap_idx, "total_swaps": total_swaps}