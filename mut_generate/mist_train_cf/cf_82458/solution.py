"""
QUESTION:
Create a function `count_peaks` that takes a list of mountain peaks where each peak is represented as a dictionary with 'name', 'ranges', and 'accessible' keys. The 'ranges' key maps to a list of mountain ranges the peak belongs to, and the 'accessible' key maps to a boolean indicating whether the peak is accessible. The function should return a dictionary where the keys are the mountain range names and the values are the total number of peaks in each range, and also return the total number of peaks.

Assume that the input data is valid and correctly formatted. The function should account for peaks that belong to multiple ranges.
"""

def count_peaks(peaks):
    """
    This function takes a list of mountain peaks and returns a dictionary where the keys are the mountain range names and the values are the total number of peaks in each range, and also returns the total number of peaks.

    Args:
        peaks (list): A list of mountain peaks where each peak is represented as a dictionary with 'name', 'ranges', and 'accessible' keys.

    Returns:
        dict: A dictionary where the keys are the mountain range names and the values are the total number of peaks in each range.
        int: The total number of peaks.
    """

    # Initialize an empty dictionary to store the count of peaks in each range
    range_count = {}
    
    # Initialize a variable to store the total number of peaks
    total_peaks = 0
    
    # Iterate over each peak in the list of peaks
    for peak in peaks:
        # Increment the total number of peaks
        total_peaks += 1
        
        # Iterate over each range the peak belongs to
        for mountain_range in peak['ranges']:
            # If the range is already in the dictionary, increment its count
            if mountain_range in range_count:
                range_count[mountain_range] += 1
            # If the range is not in the dictionary, add it with a count of 1
            else:
                range_count[mountain_range] = 1
                
    # Return the dictionary of range counts and the total number of peaks
    return range_count, total_peaks