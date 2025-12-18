"""
QUESTION:
Create a function `find_peaks` that takes a list of integers as input and returns a tuple containing the total number of peaks in the list and their respective indices. A peak is defined as an element that is greater than its immediate neighboring elements. The function should only consider elements with two neighbors, excluding the first and last elements of the list.
"""

def find_peaks(lst):
    # Initialize an empty list to store the indices of peaks
    peak_indices = []
    
    # Iterate over the indices of list from the second index to the second last
    for i in range(1, len(lst)-1):
        # If the element at the current index is greater than its neighbors, it is a peak
        if lst[i] > lst[i-1] and lst[i] > lst[i+1]:
            peak_indices.append(i)
    
    # The total number of peaks is just the length of the list of peak indices
    num_peaks = len(peak_indices)
    
    return num_peaks, peak_indices