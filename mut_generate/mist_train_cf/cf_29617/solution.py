"""
QUESTION:
Given a list of package names `packages` and a list of dependencies `dependencies` where each dependency is a tuple of two package names (the first depends on the second), write a function `install_order(packages, dependencies)` that returns the lexicographically smallest valid installation order of the packages. The function should only use the given packages and should return them in an order such that for each package, all its dependencies are installed before it.
"""

def entrance(packages, dependencies):
    graph = {package: [] for package in packages}
    in_degree = {package: 0 for package in packages}

    for dependency in dependencies:
        dependent, dependency = dependency
        graph[dependency].append(dependent)
        in_degree[dependent] += 1

    queue = [package for package in packages if in_degree[package] == 0]
    result = []

    while queue:
        package = queue.pop(0)
        result.append(package)

        for dependent in graph[package]:
            in_degree[dependent] -= 1
            if in_degree[dependent] == 0:
                queue.append(dependent)

    return result