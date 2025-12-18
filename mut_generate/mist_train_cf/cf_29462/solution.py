"""
QUESTION:
Create a function called `organize_dependencies` that takes a list of dependencies as input, where each dependency is a string in the format "dependency_name => dependency_name version", and returns a dictionary where each key is a dependency name and the corresponding value is a list of versions associated with that dependency. The input list can contain duplicate dependency names with different versions, and the function should group these versions together in the output dictionary.
"""

def organize_dependencies(dependencies):
    dependency_versions = {}
    for dependency in dependencies:
        name, version = dependency.split(" => ")
        name = name.strip()
        version = version.strip()
        if name in dependency_versions:
            dependency_versions[name].append(version)
        else:
            dependency_versions[name] = [version]
    return dependency_versions