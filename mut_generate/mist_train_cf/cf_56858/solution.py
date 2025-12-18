"""
QUESTION:
Given an array `colors` of length `n` containing distinct colors represented by integers 1, 2, and 3, and a list of queries where each query is a pair of integers `[i, c]` representing an index `i` and a target color `c`, write a function `shortestDistanceToTargetColor` that returns a list of integers representing the shortest distance from the specified index `i` to the target color `c` within the array. If no such color exists in the array, return `-1`.

Constraints:
1 <= n <= 5*10^4
1 <= colors[i] <= 3
1 <= number of queries <= 5*10^4
0 <= i < n
1 <= c <= 3
"""

import bisect

def shortestDistanceToTargetColor(colors, queries):
    color_indices = [ [], [], [] ]
    for i, color in enumerate(colors):
        color_indices[color-1].append(i)

    res = []
    for i, color in queries:
        color_ind = color_indices[color-1]
        if not color_ind: 
            res.append(-1)
            continue
        pos = bisect.bisect_left(color_ind, i)
        if pos == len(color_ind):
            closest = abs(color_ind[pos-1] - i)
        elif pos == 0:
            closest = abs(color_ind[pos] - i)
        else:
            closest = min(abs(color_ind[pos] - i), abs(color_ind[pos-1] - i))
        res.append(closest)
    
    return res