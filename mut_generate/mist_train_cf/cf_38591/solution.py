"""
QUESTION:
Implement a function `get_all_dependencies(package_name, packages)` that takes a package name and a dictionary of packages and their dependencies as input, and returns a list of all the dependencies (including transitive dependencies) for the given package. The function should handle circular dependencies and avoid duplicate dependencies in the output list. The dictionary of packages and their dependencies is structured as `{package_name: {'dependencies': [dependency1, dependency2, ...]}}`.
"""

def entrance(package_name, packages):
    visited = set()

    def dfs(package):
        if package in visited:
            return
        visited.add(package)
        for dependency in packages.get(package, {}).get('dependencies', []):
            dfs(dependency)

    dfs(package_name)
    return list(visited - {package_name})