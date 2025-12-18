"""
QUESTION:
Create a function `can_arrange` that takes a list of unique integers as input and returns a dictionary. The dictionary should contain the index of the largest element that is greater than its next element, the index of the smallest element to its right that can be swapped to fix the order, and the minimum number of swaps required to sort the list. If the list is already sorted, return {'index': -1, 'swap_with': -1, 'num_swaps': 0}.
"""

def can_arrange(arr):
    n = len(arr)
    index = -1
    swap_with = -1
    numOfSwaps = 0
    for i in range(n-1):
        if arr[i] > arr[i+1]:
            index = i
            break
    if index != -1:
        for i in range(n-1, -1, -1):
            if arr[i] < arr[index]:
                swap_with = i
                numOfSwaps = abs(swap_with - index)
                break
    return {'index': index, 'swap_with': swap_with, 'num_swaps': numOfSwaps}