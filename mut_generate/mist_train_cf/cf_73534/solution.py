"""
QUESTION:
Write a function `minTaps` that takes two parameters: an integer `n` and an array `ranges` of length `n + 1`. The function should return the minimum number of taps that need to be opened to water the entire garden of length `n`, where the `i-th` tap can irrigate the area `[i - ranges[i], i + ranges[i]]`. If it's impossible to water the entire garden, return -1. The constraints are `1 <= n <= 10^4` and `0 <= ranges[i] <= 100`.
"""

def minTaps(n, ranges):
    intervals = []
    for i in range(n + 1):
        intervals.append([i - ranges[i], i + ranges[i]])
    intervals.sort()

    end, cnt, i = 0, 0, 0
    while end < n:
        if i < len(intervals) and intervals[i][0] <= end:
            farthest = max(farthest if 'farthest' in locals() else 0, intervals[i][1])
            i += 1
        elif 'farthest' in locals() and farthest > end:
            end = farthest
            cnt += 1
        else:
            return -1
          
    return cnt + 1 if end < n else cnt