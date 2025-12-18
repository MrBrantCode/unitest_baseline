"""
QUESTION:
Create a function `install_packages(packages)` that takes a list of tuples representing software packages and their dependencies, where each tuple contains the package name and a list of its dependencies. The function should return a list of packages in the order they should be installed to satisfy all dependencies.
"""

def entrance(packages):
    graph = {pkg: set(deps) for pkg, deps in packages}
    installed = set()

    def install(pkg):
        if pkg not in installed:
            for dep in graph.get(pkg, []):
                install(dep)
            installed.add(pkg)

    for pkg, _ in packages:
        install(pkg)

    return list(installed)