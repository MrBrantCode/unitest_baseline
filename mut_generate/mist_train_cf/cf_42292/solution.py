"""
QUESTION:
Implement a function `segment_indices(signal, num_segment, sample_length)` that takes in a time series signal, the number of segments to divide it into, and a sample length, and returns a list of segment indices representing the starting index of each segment in the time series signal. The time series signal is a 1D array of numerical values, the number of segments is an integer greater than 1, and the sample length is an integer representing the length of each segment.
"""

def segment_indices(signal, num_segment, sample_length):
    segment_indices = []
    y_length = len(signal)
    hopping = (y_length - sample_length) / (num_segment - 1)  

    for i in range(num_segment):
        segment_indices.append(int(i * hopping))  

    return segment_indices