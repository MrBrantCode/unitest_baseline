"""
QUESTION:
Write a function called `find_swap_pairs(sequence)` that takes a list of unique integers as input and returns a dictionary containing the maximal index of an element that does not satisfy the non-decreasing order and the index of the preceding smaller element with which it can be swapped to potentially rectify the sequence. If no such element exists, return {'index': -1, 'swap_with': -1}.
"""

def find_swap_pairs(sequence):
    index = -1
    swap_with = -1
    for i in range(len(sequence) - 1, 0, -1):
        if sequence[i] < sequence[i-1]:
            index = i
            break
    if index != -1:
        for i in range(index - 1, -1, -1):
            if sequence[i] < sequence[index]:
                swap_with = i
                break
    return {'index': index, 'swap_with': swap_with}