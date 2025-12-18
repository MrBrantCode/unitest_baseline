"""
QUESTION:
Implement the `recursively_resolve_dependencies` function to resolve project dependencies in a software development environment. The function should take a project name and a list of already resolved dependencies as input and return a dependency tree for the given project.

The function should have the following signature: 
`def recursively_resolve_dependencies(project_name, resolved_dependencies):`

The dependency tree should be represented as a hierarchical structure where each node represents a dependency and its children represent its dependencies. 

Assume a predefined dependency tree is available for lookup. If a project does not exist in the dependency tree, return None. If a dependency has already been resolved, it should not be added to the tree.
"""

class DependencyNode:
    def __init__(self, name):
        self.name = name
        self.children = []

def recursively_resolve_dependencies(project_name, resolved_dependencies, dependency_tree):
    if project_name not in dependency_tree:
        return None

    node = DependencyNode(project_name)
    for dependency in dependency_tree[project_name]:
        if dependency not in resolved_dependencies:
            child_node = recursively_resolve_dependencies(dependency, resolved_dependencies, dependency_tree)
            if child_node:
                node.children.append(child_node)

    return node