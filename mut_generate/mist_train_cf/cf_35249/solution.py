"""
QUESTION:
Implement a module with two functions: `pretty` and `pretty_print`. The `pretty` function should take an object as input and return a string representation of the object in a human-readable format, handling nested structures and respecting a configuration option `pprint_use_unicode`. The `pretty_print` function should take an object as input and print the pretty representation of the object directly to the console by calling the `pretty` function. The `pprint_use_unicode` configuration option should default to `False` but can be set to `True` to enable the use of Unicode characters for prettier output.
"""

def pretty(obj, pprint_use_unicode=False):
    if isinstance(obj, dict):
        return "{" + ", ".join([f"{pretty(k, pprint_use_unicode)}: {pretty(v, pprint_use_unicode)}" for k, v in obj.items()]) + "}"
    elif isinstance(obj, list):
        return "[" + ", ".join([pretty(item, pprint_use_unicode) for item in obj]) + "]"
    elif isinstance(obj, tuple):
        return "(" + ", ".join([pretty(item, pprint_use_unicode) for item in obj]) + ")"
    elif isinstance(obj, str):
        return f'"{obj}"'
    else:
        return str(obj)