"""
ORIGINAL QUESTION:
Implement a Quantity Registry system with the following functions:

* `registerQuantity(name, units)`: Register a new physical quantity with its associated units. The `name` parameter is a string representing the name of the quantity, and the `units` parameter is a string representing the units associated with the quantity.
* `getUnits(name)`: Return the units associated with the given quantity name. If the quantity is not registered, return "Quantity not found".
* `getAllQuantities()`: Return a list of all registered quantities.

The system should be implemented using an efficient data structure.
"""

def entrance(name, units=None, get_all=False, quantity_name=None):
    """
    Register a new physical quantity with its associated units or retrieve units of a given quantity.

    Args:
        name (str): Name of the quantity to register (required for registration).
        units (str): Units associated with the quantity (required for registration).
        get_all (bool): If True, returns all registered quantities.
        quantity_name (str): Name of the quantity to retrieve its units (required for retrieval).

    Returns:
        str or list: Units associated with the given quantity or list of all registered quantities.
    """
    registry = entrance.registry
    if name and units:
        registry[name] = units
    elif get_all:
        return list(registry.keys())
    elif quantity_name:
        return registry.get(quantity_name, "Quantity not found")
    return None
entrance.registry = {}