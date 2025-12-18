"""
QUESTION:
In a depth-first search tree T of a connected, undirected graph G, given an edge (u, v) present in G but not in T, where pre(u) is less than pre(v), determine the truth values of the following statements about vertices u and v. 

Function name: determine_statements(u, v, T, G)
Restrictions: 
- pre(u) < pre(v)
- (u, v) is an edge in G but not in T
- T is a depth-first search tree of G
- G is a connected, undirected graph
"""

def determine_statements(u, v, T, G):
    # check if u is an ancestor of v in T
    ancestor = False
    visited = set()
    stack = [u]
    while stack:
        node = stack.pop()
        if node == v:
            ancestor = True
            break
        visited.add(node)
        for neighbor in T[node]:
            if neighbor not in visited:
                stack.append(neighbor)
                
    # check if lowest common ancestor of u and v is u
    lowest_common_ancestor = False
    if ancestor:
        stack = [u]
        while stack:
            node = stack.pop()
            if node == v:
                lowest_common_ancestor = True
                break
            for neighbor in T[node]:
                stack.append(neighbor)
                
    return ancestor, lowest_common_ancestor