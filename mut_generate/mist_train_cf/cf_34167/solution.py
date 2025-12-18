"""
QUESTION:
Implement the `resolve_dependencies` function that takes a list of packages and returns a list of package names in the order that satisfies all dependencies. If there are multiple valid orders, return any one of them. The input list consists of objects of a `Package` class with `name` and `dependencies` attributes, where each `Package` object represents a package and its dependencies.
"""

from typing import List

class Package:
    def __init__(self, name):
        self.name = name
        self.dependencies = []
        self.reverse_dependencies = []

    def add_dependency(self, package):
        self.dependencies.append(package)
        package.reverse_dependencies.append(self)

def resolve_dependencies(packages: List[Package]) -> List[str]:
    result = []
    visited = set()

    def dfs(package):
        if package.name in visited:
            return
        visited.add(package.name)
        for dep in package.dependencies:
            dfs(dep)
        result.append(package.name)

    for pkg in packages:
        dfs(pkg)

    return result[::-1]