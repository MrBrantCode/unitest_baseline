"""
QUESTION:
Implement a `resolve_arguments` function that takes a Python function signature object (`signature`) and an instance of a custom argument resolver class (`inspected_argument_resolver`) as input. The function should filter out the "self" parameter (if present) from the function signature, resolve the values of the remaining parameters using the `inspected_argument_resolver`, and return a list of resolved values in the same order as the parameters in the function signature. The `inspected_argument_resolver` has a `resolve` method that takes the parameter name and its value as arguments. The `signature` object is of type `inspect.Signature` from the `inspect` module.
"""

import inspect

def resolve_arguments(signature, inspected_argument_resolver):
    inspected_arguments = [param for param in signature.parameters if param != "self"]

    resolved_values = []
    for argument_name in inspected_arguments:
        argument_value = signature.parameters[argument_name].default
        resolved_value = inspected_argument_resolver.resolve(argument_name, argument_value)
        resolved_values.append(resolved_value)

    return resolved_values