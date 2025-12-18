"""
QUESTION:
Create a function `flatten` that takes a nested structure as input and returns a one-dimensional list. The input structure can contain lists, tuples, strings, or other nested structures. The function should ignore circular references (e.g., a list containing itself) and handle any level of nesting. Strings should be treated as atomic values that are not flattened.
"""

def flatten(nested_structure):
    seen = set()
    def visit(val):
        if not isinstance(val, (tuple, list)) or id(val) in seen:
            return [val]
        seen.add(id(val))
        result = []
        for e in val:
            result.extend(visit(e))
        return result
    return visit(nested_structure)