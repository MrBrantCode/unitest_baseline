"""
QUESTION:
Write a function explorer that takes a list of visited nodes, a graph, a current node, target coordinates (N, M), and a maximum distance K as input. The function should return True if there is a path from the current node to the target node within the maximum distance K, and False otherwise. The function should use a recursive depth-first search approach to traverse the graph. Note that the graph is represented as a list of nodes, where each node is a pair of coordinates (x, y).
"""

def explorer(visited, graph, node, N, M, K):
    if ((node[0]-N)**2+(node[1]-M)**2)**(1/2) <= K:
        return True
    if node not in visited:
        visited.append(node)
        for element in graph:
            if ((node[0]-element[0])**2+(node[1]-element[1])**2)**(1/2) <= K:
                if ((element[0]-N)**2+abs(element[1]-M)**2)**(1/2)<=K:
                    visited.append(element)
                    found_path = explorer(visited, graph, element, N, M, K)  # capture return value
                    if found_path: # if return value is True, then return it upwards in recursion
                        return True
    return False  # return False if there's no condition that met.