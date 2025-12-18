"""
QUESTION:
(This problem is the same as Minimize Malware Spread, with the differences bolded.)
In a network of nodes, each node i is directly connected to another node j if and only if graph[i][j] = 1.
Some nodes initial are initially infected by malware.  Whenever two nodes are directly connected and at least one of those two nodes is infected by malware, both nodes will be infected by malware.  This spread of malware will continue until no more nodes can be infected in this manner.
Suppose M(initial) is the final number of nodes infected with malware in the entire network, after the spread of malware stops.
We will remove one node from the initial list, completely removing it and any connections from this node to any other node.  Return the node that if removed, would minimize M(initial).  If multiple nodes could be removed to minimize M(initial), return such a node with the smallest index.
 



Example 1:
Input: graph = [[1,1,0],[1,1,0],[0,0,1]], initial = [0,1]
Output: 0


Example 2:
Input: graph = [[1,1,0],[1,1,1],[0,1,1]], initial = [0,1]
Output: 1


Example 3:
Input: graph = [[1,1,0,0],[1,1,1,0],[0,1,1,1],[0,0,1,1]], initial = [0,1]
Output: 1

 
Note:

1 < graph.length = graph[0].length <= 300
0 <= graph[i][j] == graph[j][i] <= 1
graph[i][i] = 1
1 <= initial.length < graph.length
0 <= initial[i] < graph.length
"""

from collections import deque
from typing import List

def minimize_malware_spread(graph: List[List[int]], initial: List[int]) -> int:
    def bfs(graph, seed, removed):
        queue = deque(seed)
        visited = seed
        while queue:
            node = queue.popleft()
            for next_node in range(len(graph[node])):
                if graph[node][next_node] == 0 or next_node in visited or next_node == removed:
                    continue
                visited.add(next_node)
                queue.append(next_node)
        return len(visited)
    
    best = len(graph)
    best_remove = initial[0]
    initial = set(initial)
    
    for remove_node in initial:
        initial_removed = initial - {remove_node}
        node_result = bfs(graph, initial_removed, remove_node)
        if node_result < best or (node_result == best and best_remove > remove_node):
            best = node_result
            best_remove = remove_node
    
    return best_remove