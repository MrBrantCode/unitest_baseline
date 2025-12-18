"""
QUESTION:
Write a function `find_highest_peak` that takes a list of elevations representing mountain heights in meters. The function should find the index of the highest peak in the list, returning the index of the last occurrence if there are multiple peaks with the same height. The function should have a time complexity of O(n) and a space complexity of O(1), where n is the length of the input list, and handle cases where the input list is very large (up to 10^7 elements) efficiently. Assume the input list will always contain at least one element.
"""

def find_highest_peak(elevations):
    highest_peak = elevations[0]
    highest_peak_index = 0

    for i in range(1, len(elevations)):
        if elevations[i] >= highest_peak:
            highest_peak = elevations[i]
            highest_peak_index = i

    return highest_peak_index