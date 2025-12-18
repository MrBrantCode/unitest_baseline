"""
QUESTION:
Create a function `find_highest_peak` that takes an array of elevation data as input. The function should return the index of the highest peak, where a peak is defined as an element that is greater than its two adjacent elements and is the highest among all such peaks. The input array is guaranteed to have at least three elements. The function should return -1 if no such peak exists.
"""

def find_highest_peak(elevation_data):
    highest_peak_index = -1
    for i in range(1, len(elevation_data) - 1):
        if elevation_data[i] > elevation_data[i-1] and elevation_data[i] > elevation_data[i+1]:
            if elevation_data[i] > elevation_data[highest_peak_index] or highest_peak_index == -1:
                highest_peak_index = i
    return highest_peak_index