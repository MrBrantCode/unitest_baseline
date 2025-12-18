"""
QUESTION:
Implement a function named `minMeetingRooms` that takes a list of intervals representing start and end times of meetings as input and returns the minimum number of meeting rooms required to accommodate all meetings. The input list of intervals is sorted based on their starting times. The function should have a time complexity of O(n log n), where n is the number of meetings.
"""

import heapq

def minMeetingRooms(intervals):
    intervals.sort()
    min_heap = []
    min_rooms = 0
    for interval in intervals:
        while min_heap and min_heap[0] <= interval[0]:
            heapq.heappop(min_heap)
        heapq.heappush(min_heap, interval[1])
        min_rooms = max(min_rooms, len(min_heap))
    return min_rooms