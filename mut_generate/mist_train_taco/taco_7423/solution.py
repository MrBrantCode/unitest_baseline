"""
QUESTION:
Given a list of airline tickets represented by pairs of departure and arrival airports [from, to], reconstruct the itinerary in order. All of the tickets belong to a man who departs from JFK. Thus, the itinerary must begin with JFK.

Note:


       If there are multiple valid itineraries, you should return the itinerary that has the smallest lexical order when read as a single string. For example, the itinerary ["JFK", "LGA"] has a smaller lexical order than ["JFK", "LGB"].
       All airports are represented by three capital letters (IATA code).
       You may assume all tickets form at least one valid itinerary.


Example 1:


Input: tickets = [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
Output: ["JFK", "MUC", "LHR", "SFO", "SJC"]


Example 2:


Input: tickets = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
Output: ["JFK","ATL","JFK","SFO","ATL","SFO"]
Explanation: Another possible reconstruction is ["JFK","SFO","ATL","JFK","ATL","SFO"]. But it is larger in lexical order.


Credits:
Special thanks to @dietpepsi for adding this problem and creating all test cases.
"""

import collections

def reconstruct_itinerary(tickets):
    # Create a dictionary to store the adjacency list of airports
    flight_dict = collections.defaultdict(list)
    
    # Populate the dictionary with sorted flights in reverse order
    for departure, arrival in sorted(tickets)[::-1]:
        flight_dict[departure].append(arrival)
    
    # Result deque to store the itinerary
    itinerary = collections.deque()
    
    # Recursive function to visit airports
    def visit(airport):
        while flight_dict[airport]:
            visit(flight_dict[airport].pop())
        itinerary.appendleft(airport)
    
    # Start the visit from JFK
    visit('JFK')
    
    # Convert the deque to a list and return
    return list(itinerary)