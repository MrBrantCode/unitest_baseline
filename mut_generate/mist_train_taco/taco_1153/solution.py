"""
QUESTION:
You will be given an array of non-negative integers and positive integer bin width. 

Your task is to create the Histogram method that will return histogram data corresponding to the input array. The histogram data is an array that stores under index i the count of numbers that belong to bin i. The first bin always starts with zero. 

On empty input you should return empty output.

Examples:

For input data [1, 1, 0, 1, 3, 2, 6] and binWidth=1 the result will be [1, 3, 1, 1, 0, 0, 1] as the data contains single element "0", 3 elements "1" etc.
For the same data and binWidth=2 the result will be [4, 2, 0, 1]
For input data [7] and binWidth=1 the result will be [0, 0, 0, 0, 0, 0, 0, 1]
"""

def create_histogram(data, bin_width):
    if not data:
        return []
    
    # Calculate the bin index for each number in the data
    bin_indices = [n // bin_width for n in data]
    
    # Determine the maximum bin index
    max_bin_index = max(bin_indices, default=-1) + 1
    
    # Create the histogram by counting the occurrences of each bin index
    histogram = [bin_indices.count(n) for n in range(max_bin_index)]
    
    return histogram