"""
QUESTION:
Compare two nested JSON objects considering all nested levels and data types. Implement a function that handles circular references within the JSON objects where a nested object references a parent object. The function should take two JSON objects as input and return True if they are equal and False otherwise.
"""

def are_json_objects_equal(obj1, obj2, visited=None):
    if visited is None:
        visited = set()

    if id(obj1) == id(obj2):
        return True

    if isinstance(obj1, dict) and isinstance(obj2, dict):
        if id(obj1) in visited or id(obj2) in visited:
            return True
        visited.add(id(obj1))
        visited.add(id(obj2))
        if obj1.keys() != obj2.keys():
            return False
        for key in obj1:
            if not are_json_objects_equal(obj1[key], obj2[key], visited):
                return False
        return True

    elif isinstance(obj1, list) and isinstance(obj2, list):
        if id(obj1) == id(obj2):
            return True
        if id(obj1) in visited or id(obj2) in visited:
            return True
        visited.add(id(obj1))
        visited.add(id(obj2))
        if len(obj1) != len(obj2):
            return False
        for i in range(len(obj1)):
            if not are_json_objects_equal(obj1[i], obj2[i], visited):
                return False
        return True

    else:
        return obj1 == obj2