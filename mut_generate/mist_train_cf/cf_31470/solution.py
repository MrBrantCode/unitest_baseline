"""
QUESTION:
Create a function `generate_dependency_graph(dependencies)` that takes a list of tuples representing dependency relationships as input and returns a dictionary representing the dependency graph. Each tuple in the list should have two elements, where the first element is dependent on the second element. The output dictionary should have the dependencies as keys and lists of dependencies that the key depends on as values. The function should handle duplicate dependencies by appending the dependent to the list of dependencies for the corresponding key.
"""

def generate_dependency_graph(dependencies):
    dependency_graph = {}
    
    for dependency, dependent in dependencies:
        if dependent not in dependency_graph:
            dependency_graph[dependent] = [dependency]
        else:
            dependency_graph[dependent].append(dependency)
            
        if dependency not in dependency_graph:
            dependency_graph[dependency] = []
    
    return dependency_graph