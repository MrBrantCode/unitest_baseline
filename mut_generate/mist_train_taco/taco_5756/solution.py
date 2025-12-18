"""
QUESTION:
Given N activities with their start and finish day given in array start[ ] and end[ ]. Select the maximum number of activities that can be performed by a single person, assuming that a person can only work on a single activity at a given day.
Note : Duration of the activity includes both starting and ending day.
Example 1:
Input:
N = 2
start[] = {2, 1}
end[] = {2, 2}
Output: 
1
Explanation:
A person can perform only one of the
given activities.
Example 2:
Input:
N = 4
start[] = {1, 3, 2, 5}
end[] = {2, 4, 3, 6}
Output: 
3
Explanation:
A person can perform activities 1, 2
and 4.
Your Task :
You don't need to read input or print anything. Your task is to complete the function activityselection() which takes array start[ ], array end[ ] and integer N as input parameters and returns the maximum number of activities that can be done.
Expected Time Complexity : O(N * Log(N))
Expected Auxilliary Space : O(N)
Constraints:
1 ≤ N ≤ 2*10^{5}
1 ≤ start[i] ≤ end[i] ≤ 10^{9}
"""

def activity_selection(start, end, N):
    # Create a list of activities with their start and end times
    activities = [(start[i], end[i]) for i in range(N)]
    
    # Sort activities based on their end times
    activities.sort(key=lambda x: x[1])
    
    # Initialize variables to track the last activity end time and count of activities
    last_activity_end = activities[0][1]
    count = 1
    
    # Iterate through the sorted activities to count the maximum number of activities
    for i in range(1, N):
        if activities[i][0] > last_activity_end:
            last_activity_end = activities[i][1]
            count += 1
    
    return count