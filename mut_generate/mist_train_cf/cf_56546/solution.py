"""
QUESTION:
Implement a function `findMinDifference(timePoints)` that takes a list of time points in "HH:MM" format and returns the minimum minutes difference between any two time-points in the list. The function should handle erroneous time inputs and return "Error: Invalid time input" if any time point is not in the valid range (00:00 to 23:59).
"""

def findMinDifference(timePoints):
    # Check and handle erroneous time inputs
    for t in timePoints:
        h, m = map(int, t.split(":"))
        if not (0 <= h < 24 and 0 <= m < 60):
            return "Error: Invalid time input"
    
    # Convert the time into minutes
    timePoints = sorted(int(t[:2])*60 + int(t[3:]) for t in timePoints)

    # Consider the edge case where the time is across 00:00
    timePoints += [tp+1440 for tp in timePoints[:1]]

    return min(b - a for a, b in zip(timePoints, timePoints[1:]))