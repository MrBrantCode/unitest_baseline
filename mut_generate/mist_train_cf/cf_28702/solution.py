"""
QUESTION:
Implement a function `detect_circular_dependency` that takes a dictionary `dependencies` representing the dependencies between configuration sets and returns `True` if a circular dependency exists, and `False` otherwise. The `dependencies` dictionary has configuration set names as keys and lists of names of other configuration sets on which the key configuration set depends as values. Assume the input dictionary is valid and does not contain duplicate dependencies or self-referencing sets.
"""

from typing import Dict, List

def has_circular_dependency(dependencies: Dict[str, List[str]], set_name: str, visited: set, stack: set) -> bool:
    visited.add(set_name)
    stack.add(set_name)

    for dependency in dependencies.get(set_name, []):
        if dependency not in visited:
            if has_circular_dependency(dependencies, dependency, visited, stack):
                return True
        elif dependency in stack:
            return True

    stack.remove(set_name)
    return False