"""
QUESTION:
Given a list of integer intervals `intervals` where each interval is of the form `[a, b]` with `a < b`, find the maximum size of a set `S` such that for every integer interval `A` in `intervals`, the union of `S` with `A` has a size of at most three. The function `maximumSizeOfSet` should take `intervals` as input and return the maximum size of set `S`. The intervals are subject to the following constraints: `1 <= intervals.length <= 5000`, `intervals[i].length == 2`, and `0 <= ai < bi <= 10^8`.
"""

import heapq

def maximumSizeOfSet(intervals):
    # Initialize S as an empty priority queue
    S = []

    # Sort the intervals by the start point
    intervals.sort()

    # For each interval
    for start, end in intervals:
        if S and S[0] < start:
            # If the smallest element in S is less than start,
            # pop it until it is not smaller than start.
            heapq.heappop(S)

        if len(S) < 2:
            # If the queue size is 0 or 1, then push end into the priority queue.
            heapq.heappush(S, end)
        elif S[0] < end:
            # If the smallest element in S is less than end,
            # then pop it and push end into the priority queue.
            heapq.heappop(S)
            heapq.heappush(S, end)

    # Return the size of S
    return len(S)