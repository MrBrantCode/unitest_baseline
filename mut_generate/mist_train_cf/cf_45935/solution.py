"""
QUESTION:
Given a collection of N individuals (labelled 1, 2, ..., N) and a list of dislikes where dislikes[i] = [a, b] signifies that individuals a and b should not be in the same subset, write a function `feasibleDichotomy(N, dislikes)` that returns true if it is feasible to partition all individuals into two subsets. 

The function should follow these restrictions: 
1 <= N <= 2000, 
0 <= dislikes.length <= 10000, 
dislikes[i].length == 2, 
1 <= dislikes[i][j] <= N, 
dislikes[i][0] < dislikes[i][1], 
and there are no duplicate dislike relationships (i.e., there does not exist i != j for which dislikes[i] == dislikes[j]).
"""

def feasibleDichotomy(N, dislikes):
    def dfs(node, color_to_be_assigned, color, graph):
        if color[node] != 0:
            return color[node] == color_to_be_assigned
        color[node] = color_to_be_assigned
        
        return all(dfs(v, -color_to_be_assigned, color, graph) for v in graph[node])
    
    color = {n: 0 for n in range(1, N+1)}
    graph = [[] for _ in range(N+1)]
    
    # Create adjacency list
    for u, v in dislikes:
        graph[u].append(v)
        graph[v].append(u)
        
    # Apply DFS and try to color the graph
    for node in range(1, N+1):
        if color[node] == 0 and not dfs(node, 1, color, graph):
            return False
    
    return True