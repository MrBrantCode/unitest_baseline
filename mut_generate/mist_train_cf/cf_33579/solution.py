"""
QUESTION:
Implement a function `prune_communities` that takes a graph `G` represented as an adjacency list and an integer `min_size` as input, and returns the modified graph after removing all communities (connected components) with a size less than `min_size`. The size of a community is defined as the number of nodes it contains.

The graph `G` is represented as a dictionary where each key is a node and its corresponding value is a list of neighboring nodes. The function should return a dictionary representing the modified graph after pruning the communities. 

Function Signature: `def prune_communities(G: Dict[int, List[int]], min_size: int) -> Dict[int, List[int]]`.
"""

from typing import Dict, List

def prune_communities(G: Dict[int, List[int]], min_size: int) -> Dict[int, List[int]]:
    def dfs(node, visited, community):
        visited.add(node)
        community.append(node)
        for neighbor in G[node]:
            if neighbor not in visited:
                dfs(neighbor, visited, community)

    def get_communities():
        visited = set()
        communities = []
        for node in G:
            if node not in visited:
                community = []
                dfs(node, visited, community)
                communities.append(community)
        return communities

    communities = get_communities()
    pruned_graph = {node: neighbors for node, neighbors in G.items() if len(communities[next((i for i, c in enumerate(communities) if node in c))]) >= min_size}
    return pruned_graph