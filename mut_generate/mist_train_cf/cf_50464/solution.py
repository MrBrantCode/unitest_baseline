"""
QUESTION:
Write a function `max_overlapping_events(events)` that takes a list of events as input, where each event is a list containing a start time, an end time, and a number of attendees. The function should return a tuple containing the maximum number of overlapping events and the total number of attendees during the period with the maximum overlap. The function should prioritize periods with the maximum number of attendees when there are multiple periods with the same maximum number of overlapping events. The input list can contain up to 10,000 events.
"""

import heapq

def max_overlapping_events(events):
    # Save the start (with number of attendees), end time (0 attendees) in a heap
    heap = [(start, attendees) for start, end, attendees in events]
    heap += [(end, 0) for start, end, attendees in events]
    heapq.heapify(heap)
    
    max_attendees, current_attendees = 0, 0
    max_events, current_events = 0, 0
    while heap:
        time, attendees = heapq.heappop(heap)
        if attendees > 0:
            # New event starts
            current_events += 1
            current_attendees += attendees
        else:
            # Existing event ends
            current_events -= 1
        if current_attendees > max_attendees or (current_attendees == max_attendees and current_events > max_events):
            max_attendees = current_attendees
            max_events = current_events
    return max_events, max_attendees