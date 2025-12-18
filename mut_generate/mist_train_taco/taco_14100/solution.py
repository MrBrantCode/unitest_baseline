"""
QUESTION:
JOI has a stove in your room. JOI himself is resistant to the cold, so he doesn't need to put on the stove when he is alone in the room, but he needs to put on the stove when there are visitors.

On this day, there are N guests under JOI. The ith (1 \ leq i \ leq N) visitor arrives at time T_i and leaves at time T_i + 1. There can never be more than one visitor at the same time.

JOI can turn the stove on and off at any time. However, each time you turn on the stove, you will consume one match. JOI has only K matches, so he can only stove up to K times. The stove is gone at the beginning of the day.

When the stove is on, fuel is consumed by that amount, so I want to set the time when the stove is on and off and minimize the total time when the stove is on.





Example

Input

3 2
1
3
6


Output

4
"""

def minimize_stove_time(n, k, arrival_times):
    # Calculate the differences between consecutive arrival times
    diff = []
    for i in range(n - 1):
        diff.append(arrival_times[i + 1] - arrival_times[i] - 1)
    
    # Sort the differences in descending order
    diff.sort(reverse=True)
    
    # Calculate the minimum total time the stove is on
    return n + sum(diff[k - 1:])