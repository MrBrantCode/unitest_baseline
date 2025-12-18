"""
QUESTION:
Implement a function named `functionInfo` that takes in a function name and the function itself as parameters and returns a dictionary containing metadata about the function, including the function's group and any other relevant information.

Implement a function named `processFunctions` that takes in a dictionary of functions (`funcs`), an optional group name (`group`), and an optional boolean flag (`grouped`). The function should filter and organize the functions based on the provided criteria and return the result in the following format:

- If `grouped` is `True`, return a dictionary where the keys are function groups and the values are dictionaries containing function names and their metadata.
- If `grouped` is `False`, return a dictionary where the keys are function names and the values are their metadata.

Restrictions:
- If `group` is provided, only include functions belonging to that group in the result.
- Use the `functionInfo` function to extract metadata for each function.
"""

def functionInfo(name, func):
    # Example implementation of functionInfo
    # This is a placeholder and should be replaced with actual implementation
    # Assume 'group' is a key in the metadata dictionary
    return {'group': 'math', 'other_info': '...'}

def processFunctions(funcs, group=None, grouped=False):
    result = {}
    for (name, func) in funcs.items():
        info = functionInfo(name, func)
        if group is not None and group != info['group']:
            continue

        if grouped:
            if info['group'] not in result:
                result[info['group']] = {}
            result[info['group']][name] = info
        else:
            result[name] = info
    return result