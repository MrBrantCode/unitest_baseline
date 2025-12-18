"""
QUESTION:
Design a data structure to represent a list of locations where each location has a list of neighboring locations. The data structure should efficiently store and provide the neighboring locations for each location. Implement a function `create_adjacency_list` to create this data structure.
"""

def create_adjacency_list(locations, edges):
    """
    Creates an adjacency list representation of a graph from a list of locations and edges.

    Args:
    locations (list): A list of unique location names.
    edges (list): A list of tuples, where each tuple represents a pair of connected locations.

    Returns:
    dict: An adjacency list representation of the graph.
    """

    # Initialize an empty dictionary with locations as keys
    adjacency_list = {location: [] for location in locations}

    # Populate the adjacency list with edges
    for edge in edges:
        # Assuming edge is a tuple of two locations
        location1, location2 = edge
        # Add location2 to the adjacency list of location1
        adjacency_list[location1].append(location2)
        # Add location1 to the adjacency list of location2 (for undirected graph)
        adjacency_list[location2].append(location1)

    return adjacency_list