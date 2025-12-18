"""
QUESTION:
Reconstruct a valid itinerary from a list of airline tickets. Given a list of tickets, where each ticket is a pair of departure and arrival airports, and the starting airport is "JFK", return the reconstructed itinerary as a list of strings. The function should take in a list of tickets, where each ticket is a list of two strings, and return the reconstructed itinerary.

The function name is `findItinerary` and it should take in a list of lists of strings as input, where each inner list represents a ticket with two airports. The function should return a list of strings representing the reconstructed itinerary.
"""

from collections import defaultdict

def findItinerary(tickets):
    graph = defaultdict(list)
    for pair in tickets:
        graph[pair[0]].append(pair[1])
    for key in graph:
        graph[key].sort(reverse=True)
        
    stack = ["JFK"]
    itinerary = []
    while stack:
        while graph[stack[-1]]:
            stack.append(graph[stack[-1]].pop())
        itinerary.append(stack.pop())
        
    return itinerary[::-1]