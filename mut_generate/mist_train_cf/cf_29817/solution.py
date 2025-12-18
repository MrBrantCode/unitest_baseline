"""
QUESTION:
Implement the `build_order` function, which takes a list of targets where each target is a dictionary containing a "target_name" and a list of its dependencies. Return a list representing the order in which the targets should be built, such that a target is built after all its dependencies have been built. If a target has no dependencies, it can be built immediately. Assume the input is a list of dictionaries with the keys "target_name" and "dependencies". The input does not contain any circular dependencies.
"""

def build_order(targets):
    dependency_map = {target["target_name"]: set(target["dependencies"]) for target in targets}
    built = set()
    order = []

    def build_target(target_name):
        if target_name not in built:
            for dependency in dependency_map[target_name]:
                build_target(dependency)
            order.append(target_name)
            built.add(target_name)

    for target in targets:
        build_target(target["target_name"])

    return order