"""
QUESTION:
Write a function `find_cheapest_itinerary(flights, start, end)` that takes a list of tuples representing flight routes, a starting airport, and a destination airport. The function should return a tuple containing the total cost and the itinerary for the cheapest trip from the starting airport to the destination airport. If there are multiple cheapest itineraries, return the one with the lexicographically smallest itinerary.

The function should take the following parameters:
- `flights`: A list of tuples, where each tuple contains the source airport, destination airport, and the cost of the flight.
- `start`: A string representing the starting airport.
- `end`: A string representing the destination airport.

The function should return a tuple containing the total cost and the itinerary as a list of airport codes.
"""

import heapq

def find_cheapest_itinerary(flights, start, end):
    graph = {}
    for source, dest, cost in flights:
        if source not in graph:
            graph[source] = []
        graph[source].append((dest, cost))

    heap = [(0, start, [])]
    while heap:
        total_cost, curr, path = heapq.heappop(heap)
        if curr == end:
            return total_cost, path + [end]
        for neighbor, cost in graph.get(curr, []):
            heapq.heappush(heap, (total_cost + cost, neighbor, path + [curr]))