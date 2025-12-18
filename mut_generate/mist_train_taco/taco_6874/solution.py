"""
QUESTION:
Given a list of 24-hour clock time points in "Hour:Minutes" format, find the minimum minutes difference between any two time points in the list. 

Example 1:

Input: ["23:59","00:00"]
Output: 1



Note:

The number of time points in the given list is at least 2 and won't exceed 20000.
The input time is legal and ranges from 00:00 to 23:59.
"""

def find_min_time_difference(time_points):
    if len(time_points) > 1440:
        return 0
    
    # Convert time points to minutes since midnight
    time_num = [60 * int(time[:2]) + int(time[3:]) for time in time_points]
    
    # Sort the time points in minutes
    time_num.sort()
    
    # Initialize the minimum difference to a large value
    min_diff = 24 * 60
    
    # Calculate the minimum difference between consecutive time points
    for i in range(len(time_num) - 1):
        min_diff = min(min_diff, time_num[i + 1] - time_num[i])
    
    # Consider the circular difference (between the last and the first time point)
    min_diff = min(min_diff, 24 * 60 + time_num[0] - time_num[-1])
    
    return min_diff