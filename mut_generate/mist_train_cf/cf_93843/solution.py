"""
QUESTION:
Write a function `find_highest_peak` that takes in a list of elevations representing the heights of mountains in meters and returns the index of the highest peak. If there are multiple peaks with the same height, return the index of the last occurrence. The function should have a time complexity of O(n) and a space complexity of O(1), where n is the length of the input list. The input list will always contain at least one element.
"""

def find_highest_peak(elevations):
    highest_peak_index = 0
    highest_peak_height = elevations[0]
    
    for i in range(1, len(elevations)):
        if elevations[i] > highest_peak_height:
            highest_peak_index = i
            highest_peak_height = elevations[i]
        elif elevations[i] == highest_peak_height:
            highest_peak_index = i
    
    return highest_peak_index