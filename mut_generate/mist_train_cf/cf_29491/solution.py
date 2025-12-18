"""
QUESTION:
Write a function `valid_ordering(dependencies)` that takes a list of strings representing dependencies between items in the form "A depends on B" and returns a valid ordering as a comma-separated string if one exists. Assume the input list will not contain any circular dependencies.
"""

def valid_ordering(dependencies):
    def find_order(item, dependency_map, ordered_items):
        if item in ordered_items:
            return ordered_items
        if item in dependency_map:
            ordered_items = find_order(dependency_map[item], dependency_map, ordered_items)
        ordered_items.append(item)
        return ordered_items

    dependency_map = {}
    for dependency in dependencies:
        item, depends_on = dependency.split(" depends on ")
        dependency_map[item] = depends_on

    ordered_items = []
    for item in dependency_map:
        if item not in ordered_items:
            ordered_items = find_order(item, dependency_map, ordered_items)

    return ", ".join(ordered_items)