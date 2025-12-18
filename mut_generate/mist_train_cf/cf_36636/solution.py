"""
QUESTION:
Implement a function `build_order` that takes a dictionary of source files and their dependencies as input, where each key is a source file and its corresponding value is a list of dependencies. The function should return a list representing the order in which the source files should be built. If a circular dependency is detected, return the message "Circular dependency detected, unable to build."
"""

from collections import defaultdict, deque

def build_order(project):
    dependencies = defaultdict(list)
    dependents = defaultdict(list)
    for source, deps in project.items():
        dependencies[source] = deps
        for dep in deps:
            dependents[dep].append(source)

    build_order = []
    ready_to_build = deque([source for source, deps in dependencies.items() if not deps])

    while ready_to_build:
        source = ready_to_build.popleft()
        build_order.append(source)
        for dependent in dependents[source]:
            dependencies[dependent].remove(source)
            if not dependencies[dependent]:
                ready_to_build.append(dependent)

    if len(build_order) == len(project):
        return build_order
    else:
        return "Circular dependency detected, unable to build."