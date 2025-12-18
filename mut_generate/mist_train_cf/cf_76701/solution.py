"""
QUESTION:
Implement a function `deleteTreeNodes` that takes three parameters: an integer `nodes` representing the number of nodes in a tree, a list `parent` representing the parent-child relationships in the tree, and a list `value` representing the values of each node in the tree. The function should return the number of nodes in the tree after deleting all subtrees with a sum of zero and the maximum sum of the remaining subtrees.

Restrictions: The input lists `parent` and `value` are guaranteed to have the same length as the number of nodes in the tree. The `parent` list represents the parent of each node, where `-1` indicates the root node. The `value` list represents the value of each node.
"""

from typing import List, Tuple
import collections

def deleteTreeNodes(nodes: int, parent: List[int], value: List[int]) -> Tuple[int, int]:
    adjacencyList = collections.defaultdict(list)
    for i in range(len(parent)):
        if parent[i] != -1: 
            adjacencyList[parent[i]].append(i)

    def dfs(node):
        totalNodes = 1
        subTreeSum = value[node]

        # Recursive case: Perform DFS for all children nodes
        for child in adjacencyList[node]:
            childNodes, childSubTreeSum = dfs(child)
            totalNodes += childNodes
            subTreeSum += childSubTreeSum
        
        # Returns results of DFS on this node
        if subTreeSum == 0: 
            return 0, 0
        return totalNodes, subTreeSum
    
    maxSubTreeSum = float('-inf')
    totalNodes, subTreeSum = dfs(0)
    maxSubTreeSum = max(maxSubTreeSum, subTreeSum)
    if subTreeSum == 0:
        return 0, 0
    return totalNodes, maxSubTreeSum