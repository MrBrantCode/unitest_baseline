"""
QUESTION:
Find a function `findItinerary` that takes a list of airline tickets `tickets` where each ticket is a list containing the departure airport, arrival airport, and travel time. Reconstruct the itinerary in order, starting from "JFK", with the smallest total travel time. If multiple itineraries have the same total travel time, return the one with the smallest lexical order when read as a single string. All tickets must be used exactly once.

The input list `tickets` has the following restrictions:
- `1 <= tickets.length <= 300`
- Each ticket is a list of three elements: `[from, to, time]`
- `from` and `to` are three-letter strings consisting of uppercase English letters
- `time` is a positive integer
- `from` and `to` are not the same airport
"""

import collections
import heapq

def findItinerary(tickets):
    flights = collections.defaultdict(list)
    for start, end, time in sorted(tickets)[::-1]:
        heapq.heappush(flights[start], (time, end))
    route, stack = [], ['JFK']
    while stack:
        while flights[stack[-1]]:
            _, end = heapq.heappop(flights[stack[-1]])
            stack.append(end)
        route.append(stack.pop())
    return route[::-1]