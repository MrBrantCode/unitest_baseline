"""
QUESTION:
Implement the `string_expansion` function that takes in an input string `expanded`, a context object `context`, and a default value `default`. The function replaces placeholders in the input string of the form `${group.key}` with the corresponding values from the context object. If the group is "Params", the values are retrieved from `context.Descriptor.Parameters`; if the group is "Publish", the values are retrieved from `context.params`; otherwise, the values are retrieved from `context.params`. If the value is not found in the context object, the default value is used.

Function Signature: `def string_expansion(expanded: str, context: Context, default: str) -> str`
"""

import re

def string_expansion(expanded: str, context: object, default: str) -> str:
    for match in re.finditer(r'\${(.*?)\.(.*?)}', expanded):
        group, key = match.groups()
        if group == "Params":
            collection = getattr(context, 'Descriptor', None) and getattr(context.Descriptor, 'Parameters', None)
        elif group == "Publish":
            collection = getattr(context, 'params', None)
        else:
            collection = getattr(context, 'params', None)

        value = collection.get(key, default) if collection is not None else f'<<UNKNOWN GROUP {group}>>'
        expanded = expanded.replace(match.group(0), str(value))

    return expanded