"""
QUESTION:
Find all direct and transitive dependencies of a given package in a dictionary of package dependencies.

Given a dictionary `dependencies` where keys are package names and values are lists of the package's dependencies, and a string `package` representing the package name, write a function `find_dependencies(dependencies, package)` that returns a list of all the direct and transitive dependencies of the given package. The returned list should not contain the package itself and should not contain duplicate values.
"""

def find_dependencies(dependencies, package):
    direct_dependencies = dependencies.get(package, [])
    transitive_dependencies = []
    
    def get_transitive_deps(pkg):
        nonlocal transitive_dependencies
        for dep in dependencies.get(pkg, []):
            if dep not in transitive_dependencies:
                transitive_dependencies.append(dep)
                get_transitive_deps(dep)
    
    get_transitive_deps(package)
    return list(set(direct_dependencies + transitive_dependencies))