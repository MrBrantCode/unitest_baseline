"""
QUESTION:
Build a function `build_dependency_graph(dependencies)` that takes a list of dependencies as input, where each dependency is a tuple containing a module name and a version number. The function should return a dictionary representing the dependency graph, where each key is a module name and its corresponding value is a list of tuples. Each tuple should contain a version number and a list of modules that depend on it.
"""

def build_dependency_graph(dependencies):
    dependency_graph = {}
    
    for module, version in dependencies:
        if module not in dependency_graph:
            dependency_graph[module] = []
        
        for key, value in dependency_graph.items():
            if key != module:
                for index, (ver, deps) in enumerate(value):
                    if ver == version:
                        dependency_graph[key][index] = (ver, deps + [module])
        
        dependency_graph[module].append((version, []))
    
    return dependency_graph