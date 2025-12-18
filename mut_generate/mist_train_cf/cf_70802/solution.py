"""
QUESTION:
Implement the function `canAttendMeetings(intervals)` that takes an array of meeting time intervals, where each interval is a list of two integers representing the start and end times. Return `True` if a person can attend all the meetings without any overlap, and `False` otherwise.

The intervals array has the following restrictions: 
- The length of intervals is between 0 and 10^4 (inclusive).
- Each interval has a length of 2.
- The start time is less than the end time, and both times are between 0 and 10^6 (inclusive).
"""

def canAttendMeetings(intervals):
    intervals.sort(key=lambda x: x[0])
    
    for i in range(1, len(intervals)):
        if intervals[i][0] < intervals[i-1][1]: 
            return False
    
    return True