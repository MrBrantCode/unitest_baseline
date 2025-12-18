"""
QUESTION:
Implement a function `findItinerary` that takes a list of airline tickets, represented as pairs of departure and arrival airports, and returns the reconstructed itinerary in order, starting from the departure airport "JFK". The input list of tickets forms a valid itinerary.
"""

from collections import defaultdict

def findItinerary(tickets):
    """
    Reconstructs a valid itinerary from a list of airline tickets.
    
    Args:
    tickets (list): A list of airline tickets, where each ticket is a list containing the departure and arrival airports.
    
    Returns:
    list: The reconstructed itinerary in order, starting from the departure airport "JFK".
    """
    ticket = defaultdict(list)
    for fr, to in tickets:
        ticket[fr].append(to)
    for k in ticket.keys():
        ticket[k].sort(reverse=True)

    ans = []

    def dfs(f):
        while len(ticket[f]) != 0:
            dfs(ticket[f].pop())
        ans.append(f)

    dfs("JFK")
    return ans[::-1]