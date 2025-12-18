"""
QUESTION:
Implement the `expose_methods` decorator function that takes a list of module names as input. The function should dynamically expose all the methods from the specified modules, making them accessible through a dictionary where the keys are the module names and the values are lists of exposed method names. The exposed methods dictionary should be assigned to the `exposed_methods` attribute of the decorated function.
"""

def expose_methods(modules):
    exposed_methods = {}

    for module_name in modules:
        module = globals()[module_name]
        exposed_methods[module_name] = [method for method in dir(module) if callable(getattr(module, method)) and not method.startswith('__')]

    return exposed_methods