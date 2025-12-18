"""
QUESTION:
There is one meeting room in a firm. There are N meetings in the form of (start[i], end[i]) where start[i] is start time of meeting i and end[i] is finish time of meeting i.
What is the maximum number of meetings that can be accommodated in the meeting room when only one meeting can be held in the meeting room at a particular time? 
Note: Start time of one chosen meeting can't be equal to the end time of the other chosen meeting.
Example 1:
Input:
N = 6
start[] = {1,3,0,5,8,5}
end[] =  {2,4,6,7,9,9}
Output: 
4
Explanation:
Maximum four meetings can be held with
given start and end timings.
The meetings are - (1, 2),(3, 4), (5,7) and (8,9)
Example 2:
Input:
N = 3
start[] = {10, 12, 20}
end[] = {20, 25, 30}
Output: 
1
Explanation:
Only one meetings can be held
with given start and end timings.
Your Task :
You don't need to read inputs or print anything. Complete the function maxMeetings() that takes two arrays start[] and end[] along with their size N as input parameters and returns the maximum number of meetings that can be held in the meeting room.
Expected Time Complexity : O(N*LogN)
Expected Auxilliary Space : O(N)
Constraints:
1 ≤ N ≤ 10^{5}
0 ≤ start[i] < end[i] ≤ 10^{5}
"""

def max_meetings(start, end, N):
    # Combine start and end times into a list of tuples
    meets = list(zip(start, end))
    
    # Sort the meetings by their end times
    meets.sort(key=lambda x: x[1])
    
    # Initialize variables to keep track of the maximum number of meetings
    max_meetings_count = 0
    last_end_time = float('-inf')
    
    # Iterate through the sorted meetings
    for i in range(N):
        # If the start time of the current meeting is greater than the last end time
        if meets[i][0] > last_end_time:
            # Increment the count of maximum meetings
            max_meetings_count += 1
            # Update the last end time to the end time of the current meeting
            last_end_time = meets[i][1]
    
    # Return the maximum number of meetings that can be held
    return max_meetings_count