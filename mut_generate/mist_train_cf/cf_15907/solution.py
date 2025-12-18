"""
QUESTION:
Implement a function named `compare_json` to compare two nested JSON objects in Python. The function should recursively iterate through all levels of the objects, compare their values, and handle circular references where a nested object references a parent object. It should also handle different data types and return a boolean indicating whether the two JSON objects are equal. The function should not modify the input objects and should not throw any exceptions.
"""

def compare_json(obj1, obj2, visited=None):
    if visited is None:
        visited = []

    # Check for circular references
    if id(obj1) in visited or id(obj2) in visited:
        return True

    visited.append(id(obj1))
    visited.append(id(obj2))

    if type(obj1) != type(obj2):
        return False

    if isinstance(obj1, dict):
        if len(obj1) != len(obj2):
            return False
        for key in obj1:
            if key not in obj2 or not compare_json(obj1[key], obj2[key], visited):
                return False
        return True

    if isinstance(obj1, list):
        if len(obj1) != len(obj2):
            return False
        for i in range(len(obj1)):
            if not compare_json(obj1[i], obj2[i], visited):
                return False
        return True

    return obj1 == obj2