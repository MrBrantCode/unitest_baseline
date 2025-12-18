"""
QUESTION:
Write a function `maxDistToClosest` that takes an array `seats` where `seats[i] = 1` represents a person sitting in the `i-th` seat, and `seats[i] = 0` represents that the `i-th` seat is empty. The function should return the maximum distance to the closest person that Alex can achieve by sitting in an empty seat. The distance between two seats `i` and `j` is `|i - j|`. 

Constraints: `2 <= seats.length <= 2 * 10^4`, `seats[i]` is `0` or `1`, at least one seat is empty, and at least one seat is occupied.
"""

def maxDistToClosest(seats):
    N = len(seats)
    left, right = [0]*N, [0]*N
    
    distance = N
    for i in range(N):
        if seats[i] == 1:
            distance = 0
        else:
            distance += 1
        left[i] = distance 

    distance = N
    for i in range(N-1, -1, -1):
        if seats[i] == 1:
            distance = 0
        else:
            distance += 1
        right[i] = distance 

    return max(min(left[i], right[i]) for i in range(N) if seats[i] == 0)