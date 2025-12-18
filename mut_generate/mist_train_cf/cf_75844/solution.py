"""
QUESTION:
Given a number of individuals (N) and a list of dislikes where dislikes[i] = [a, b] signifies that individuals a and b cannot be assigned to the same group, write a function `possibleBipartition(N, dislikes)` to determine if it's feasible to divide everyone into two groups under these conditions. The function should return `True` if it's possible and `False` if it's not.

Restrictions:
- 1 <= N <= 2000
- 0 <= dislikes.length <= 10000
- dislikes[i].length == 2
- 1 <= dislikes[i][j] <= N
- dislikes[i][0] < dislikes[i][1]
- There does not exist i != j for which dislikes[i] == dislikes[j].
"""

def possibleBipartition(N, dislikes):
    graph = [[] for _ in range(N+1)]
    colors = [0 for _ in range(N+1)]
    
    for dislike in dislikes:
        graph[dislike[0]].append(dislike[1])
        graph[dislike[1]].append(dislike[0])
        
    def dfs(node, color):
        colors[node] = color
        for neigh in graph[node]:
            if colors[neigh] == color: 
                return False
            if colors[neigh] == 0 and not dfs(neigh, -color): 
                return False
        return True
    
    for node in range(1, N+1):
        if colors[node] == 0 and not dfs(node, 1):
            return False
            
    return True