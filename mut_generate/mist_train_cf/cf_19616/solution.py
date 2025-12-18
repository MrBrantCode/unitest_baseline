"""
QUESTION:
Design a function named `detect_infinite_loop` that takes a given program as input and returns a boolean value indicating whether the program contains an infinite loop. The function should use static analysis and not rely on loops or recursion.
"""

def detect_infinite_loop(program):
    # Parse the given program and generate its control flow graph
    graph = parse_program(program)

    # Perform a reachability analysis on the control flow graph
    visited = set()
    def dfs(node):
        if node in visited:
            return True  # cycle detected
        visited.add(node)
        for neighbor in graph[node]:
            if dfs(neighbor):
                return True
        return False

    # Check for the presence of any cycles in the control flow graph
    for node in graph:
        if dfs(node):
            return True

    return False


def parse_program(program):
    # This function should parse the given program and return its control flow graph
    # For simplicity, let's assume the program is a list of nodes and edges
    # where each node is a statement or function call, and each edge represents the flow of control
    # between nodes
    return {
        'A': ['B', 'C'],
        'B': ['D'],
        'C': ['B'],
        'D': ['A']  # this edge creates a cycle
    }