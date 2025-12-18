"""
QUESTION:
Write a function named check_euler that takes the number of nodes in a fully connected undirected graph as input and returns True if the graph is guaranteed to possess an Euler circuit and False otherwise. Assume that the input will always be a positive integer.
"""

def check_euler(nodes):
    # All nodes in a fully-connected graph will have degree (nodes - 1)
    degree = nodes - 1
    
    # A graph will have Euler circuit if all nodes have even degree.
    return degree % 2 == 0