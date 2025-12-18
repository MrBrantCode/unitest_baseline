"""
QUESTION:
Design a function `find_peaks` that takes a list of numbers as input and returns a list of tuples, where each tuple contains the index and value of a peak in the list. A peak is defined as a value that is greater than its neighboring elements. The function should return an empty list if the input list has fewer than 3 elements. The function should consider only the elements that have both a previous and a next neighbor.
"""

def find_peaks(lst):
    if len(lst) < 3:
        return []  

    peaks = []  

    for i in range(1, len(lst)-1):
        if lst[i-1] < lst[i] > lst[i+1]:  
            peaks.append((i, lst[i]))  

    return peaks