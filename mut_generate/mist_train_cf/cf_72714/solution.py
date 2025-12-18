"""
QUESTION:
Create a function `find_peaks` that takes a list of integers as input and returns the count and position of peaks in the list. A peak is defined as a value that is greater than its adjacent numbers. The function should exclude the first and last elements in the list, as they do not have two neighbors to compare with. The position of peaks should be 0-indexed.
"""

def find_peaks(lst):
    peaks = []
    for i in range(1, len(lst)-1):  # exclude first and last element
        if lst[i]>lst[i-1] and lst[i]>lst[i+1]:  # greater than neighbors
            peaks.append((i, lst[i]))
    return len(peaks), peaks