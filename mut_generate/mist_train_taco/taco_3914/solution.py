"""
QUESTION:
An infinite army of ants is marching on an infinite 2-D plane. Since ants are disciplined, here's how they march: each ant chooses exactly one x coordinate and moves along it in positive y direction, starting from (x, 0). There exists exactly one ant for each x coordinate on that plane and hence there are infinite ants!

There are N horizontal barriers lying on this plane. The i^th barrier is defined by (xi, yi) and di, which means that the barrier is blocking all ants which want to pass through points lying on line segment connecting (xi, yi) and (xi + di, yi). Once an ant encounters a barrier, it stops moving.

Given all the barriers, your task is to find the total number of ants, that will be ever blocked at some point in their march.

INPUT

The first line contains an integer N which denotes the number of barriers. Next N lines follow, each contains 3 space separated integers,  "xi yi di" as explained in problem statement above.

Note: The barriers in the input may overlap.

OUTPUT

Output a single integer, the number of ants that will be ever blocked at some point in their march.

CONSTRAINTS

1 ≤ N ≤ 10^5
1 ≤ xi, yi, di ≤ 10^9

SAMPLE INPUT
2
1 1 4
7 3 5

SAMPLE OUTPUT
11

Explanation

Here 5 ants will be blocked on points (1,1) , (2, 1) , (3, 1), (4, 1) and (5, 1).

6 ants will be blocked on (7, 3), (8, 3), (9, 3), (10, 3), (11, 3), (12, 3).

In total, 11 ants are blocked in their journey.
"""

def count_blocked_ants(barriers):
    # Extract and sort barriers based on the starting x-coordinate
    sorted_barriers = sorted((x, d) for x, y, d in barriers)
    
    # Initialize variables to track the total number of blocked ants
    total_blocked_ants = 0
    last_end = -1
    
    for start, d in sorted_barriers:
        if start > last_end:
            # If the current barrier starts after the last one ends, add all its ants
            total_blocked_ants += d + 1
            last_end = start + d
        elif start <= last_end and start + d > last_end:
            # If the current barrier overlaps with the last one, add only the non-overlapping ants
            total_blocked_ants += start + d - last_end
            last_end = start + d
    
    return total_blocked_ants