"""
QUESTION:
Write a function `minMeetingRooms` that takes a list of intervals representing start and end times of meetings as input, where each interval is a list of two integers `[start, end]` and the list is sorted based on the start times. The function should return the minimum number of meeting rooms required to accommodate all the meetings. The function should run in a time complexity of O(n log n) or better.
"""

import heapq

def minMeetingRooms(intervals):
    intervals.sort()
    min_heap = []
    min_rooms = 0
    for interval in intervals:
        # Pop all meetings that have ended
        while min_heap and min_heap[0] <= interval[0]:
            heapq.heappop(min_heap)
        # Add the current meeting's end time to the Min Heap
        heapq.heappush(min_heap, interval[1])
        # Update the minimum number of rooms required
        min_rooms = max(min_rooms, len(min_heap))
    return min_rooms