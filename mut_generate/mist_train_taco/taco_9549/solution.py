"""
QUESTION:
Given the start time st and end time et of a race in the format hh:mm:ss. You task is to print the time taken to complete the race.
Example 1:
Input: st = 13:50:45
et = 14:55:50
Output: 01:05:05
Explaination: The time gap is 1 hour 5 
minutes and 5 seconds.
Example 2:
Input: st = 12:00:00
et = 24:00:00
Output: 12:00:00
Explaination: The time gap is of 12 hours.
Your Task:
You do not need to read input or print anything. Your task is to complete the function timeGap() which takes st and et as input parameters and returns the time difference between them.
Expected Time Complexity: O(1)
Expected Auxiliary Space: O(1)
Constraints:
0 ≤ hh ≤ 24
0 ≤ mm ≤ 59
0 ≤ ss ≤ 59
"""

import time

def calculate_time_gap(st: str, et: str) -> str:
    # Split the start and end times into hours, minutes, and seconds
    start_time_parts = st.split(':')
    end_time_parts = et.split(':')
    
    # Convert the start time parts to total seconds
    start_seconds = int(start_time_parts[0]) * 3600 + int(start_time_parts[1]) * 60 + int(start_time_parts[2])
    
    # Convert the end time parts to total seconds
    end_seconds = int(end_time_parts[0]) * 3600 + int(end_time_parts[1]) * 60 + int(end_time_parts[2])
    
    # Calculate the difference in seconds
    total_seconds_diff = end_seconds - start_seconds
    
    # Convert the total seconds difference back to the format "hh:mm:ss"
    time_gap = time.strftime('%H:%M:%S', time.gmtime(total_seconds_diff))
    
    return time_gap