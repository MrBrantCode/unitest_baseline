"""
QUESTION:
Implement a function `parse_dependencies(dependency_list)` that takes a list of dependency specifications in the format `(package_name, type={'type': (dependency-type1, dependency-type2, ...)})` and returns a dictionary representing the dependencies. The dictionary should have package names as keys and the types of dependencies as values. If a package has multiple types of dependencies, the value should be a list of those types. Assume that the input dependency_list is a list of tuples, where the first element is the package name and the second element is a dictionary containing a 'type' key with a tuple of dependency types.
"""

def parse_dependencies(dependency_list):
    dependencies = {}
    for dependency in dependency_list:
        package_name = dependency[0]
        dependency_types = dependency[1]['type'] if 'type' in dependency[1] else []
        dependencies[package_name] = dependency_types
    return dependencies