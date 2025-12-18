"""
QUESTION:
Implement a Python class `EntityRegistry` with methods to register and retrieve entity types and their options. The class should have a method `register` that takes three parameters: `entity_type`, `options`, and `menu_enabled`. It should store the registered entity types and their options in a data structure. The class should also have a method `get_registered_entities` that returns a dictionary containing the registered entity types as keys and their options as values.
"""

def entrance(entity_type, options, menu_enabled):
    registered_entities = {entity_type: {'options': options, 'menu_enabled': menu_enabled}}
    return registered_entities