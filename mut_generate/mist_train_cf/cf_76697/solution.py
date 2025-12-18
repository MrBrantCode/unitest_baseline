"""
QUESTION:
Implement a function `minMeetingRooms(intervals)` that takes an array of meeting time intervals as input where `intervals[i] = [starti, endi]`, and returns the minimum number of conference rooms needed to accommodate all meetings without overlap.

Constraints:
- `1 <= intervals.length <= 10^4`
- `0 <= starti < endi <= 10^6`
"""

import heapq

def minMeetingRooms(intervals):
    if not intervals:
        return 0
    intervals.sort()
    heap = []
    heapq.heappush(heap, intervals[0][1])
    for i in range(1, len(intervals)):
        if intervals[i][0] >= heap[0]:
            heapq.heappop(heap)
        heapq.heappush(heap, intervals[i][1])
    return len(heap)