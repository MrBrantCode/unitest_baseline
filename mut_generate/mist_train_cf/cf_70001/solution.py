"""
QUESTION:
Create a function named `calcEquation` that takes in three parameters: `equations`, `values`, and `queries`. 

The `equations` parameter is a list of lists, where each sublist contains two strings representing variables. The `values` parameter is a list of real numbers corresponding to the `equations` list, where `values[i]` represents the value of `equations[i][0]` divided by `equations[i][1]`. 

The `queries` parameter is another list of lists, where each sublist contains two strings representing variables to be evaluated. The function should return a list of real numbers, where each number corresponds to the result of the division of the two variables in the `queries` list. If a result cannot be determined, the function should return `-1.0`. 

Assume that the inputs are valid and that the evaluation of the queries will not result in division by zero and there will be no contradiction.
"""

from collections import defaultdict

def calcEquation(equations, values, queries):
    """
    This function calculates the result of division of variables in the queries list.

    Parameters:
    equations (list): A list of lists, where each sublist contains two strings representing variables.
    values (list): A list of real numbers corresponding to the equations list.
    queries (list): A list of lists, where each sublist contains two strings representing variables to be evaluated.

    Returns:
    list: A list of real numbers, where each number corresponds to the result of the division of the two variables in the queries list.
    If a result cannot be determined, the function returns -1.0.
    """
    
    # Create a graph with variables as nodes and edges weighted with their corresponding values
    graph = defaultdict(dict)
    for (var1, var2), value in zip(equations, values):
        graph[var1][var2] = value
        graph[var2][var1] = 1 / value  # Inverse of the original value

    def dfs(var1, var2, visited):
        # If var1 is not in the graph or var2 is not reachable from var1, return -1.0
        if var1 not in graph or var2 not in graph:
            return -1.0
        
        # If var1 and var2 are already connected, return their ratio
        if var2 in graph[var1]:
            return graph[var1][var2]
        
        # Mark var1 as visited to avoid infinite loops
        visited.add(var1)
        
        # Explore all neighbors of var1
        for neighbor in graph[var1]:
            if neighbor not in visited:
                # Recursively explore the neighbor
                temp = dfs(neighbor, var2, visited)
                # If var2 is reachable from the neighbor, return the product of their ratios
                if temp != -1.0:
                    return graph[var1][neighbor] * temp
        
        # If var2 is not reachable from var1, return -1.0
        return -1.0

    # Evaluate each query using depth-first search
    results = []
    for var1, var2 in queries:
        # Use a set to keep track of visited variables
        visited = set()
        results.append(dfs(var1, var2, visited))
    
    return results