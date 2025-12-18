"""
QUESTION:
Find the function `highestAltitude` that takes an integer array `gain` of length `n` where `gain[i]` is the net gain in altitude between points `i` and `i + 1`, and returns the highest altitude of a point and the corresponding point as a tuple. If there are multiple points with the same highest altitude, return the point with the smallest index. The length of `gain` is between 1 and 100, and the values in `gain` are between -100 and 100.
"""

def highestAltitude(gain):
    altitudes = [sum(gain[:i+1]) for i in range(len(gain))]
    altitudes.insert(0, 0)  
    highest_altitude = max(altitudes)
    return highest_altitude, altitudes.index(highest_altitude)