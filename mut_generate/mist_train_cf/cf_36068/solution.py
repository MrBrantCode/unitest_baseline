"""
QUESTION:
Write a function `RemoveDuplicateChildren(graph)` that takes a `Graph` object as input and removes any duplicate child nodes from the graph, where a duplicate child node is a node that is added to multiple parent nodes. The function should return the modified graph object with the duplicate child nodes removed. The function assumes that the `Graph` class has a `nodes` attribute that is a dictionary where the keys are parent nodes and the values are lists of child nodes.
"""

def RemoveDuplicateChildren(graph):
    child_to_parent = {}
    duplicates = set()
    
    for parent, children in graph.nodes.items():
        for child in children:
            if child in child_to_parent:
                duplicates.add(child)
            else:
                child_to_parent[child] = parent
    
    for parent, children in graph.nodes.items():
        graph.nodes[parent] = [child for child in children if child not in duplicates]
    
    return graph