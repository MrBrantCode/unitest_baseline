"""
QUESTION:
Write a function called `find_highest_peak` that takes a list of elevations as input and returns the index of the highest peak. If there are multiple peaks with the same height, return the index of the last occurrence. The function should have a time complexity of O(n) and a space complexity of O(1), where n is the length of the input list.
"""

def find_highest_peak(elevations):
    highest_peak = elevations[0]
    highest_peak_index = 0

    for i in range(1, len(elevations)):
        if elevations[i] > highest_peak:
            highest_peak = elevations[i]
            highest_peak_index = i

    return highest_peak_index