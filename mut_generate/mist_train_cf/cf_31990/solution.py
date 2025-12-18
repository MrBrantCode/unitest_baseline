"""
QUESTION:
Create a function `createList` that takes a list of parameters as input and returns a new list. The function should process each parameter according to the following rules:
- If the parameter is a positive integer, add it to the new list.
- If the parameter is a string, add its length to the new list.
- If the parameter is a list, recursively apply the above rules to its elements and add the results to the new list.

Note: The function should handle nested lists of arbitrary depth.
"""

def createList(params):
    result = []
    for param in params:
        if isinstance(param, int) and param > 0:
            result.append(param)
        elif isinstance(param, str):
            result.append(len(param))
        elif isinstance(param, list):
            result.extend(createList(param))
    return result