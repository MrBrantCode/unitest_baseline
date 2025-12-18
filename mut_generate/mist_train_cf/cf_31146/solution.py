"""
QUESTION:
Implement a `TabPermissions` class with the following methods: `contains(self, tab, permission)`, `getAll(self, tab)`, `remove(self, tab, permission)`, and `request(self, tab, permission)`. The class should have a dictionary attribute `functions` to store the available functions and a dictionary attribute `types` to store the types of tabs. The class should manage permissions for different types of tabs and pass the given test cases. The `contains` method should return `True` if the given `tab` contains the specified `permission`, otherwise `False`. The `getAll` method should return a list of all permissions associated with the given `tab`. The `remove` method should remove the specified `permission` from the given `tab`. The `request` method should add the specified `permission` to the given `tab`.
"""

def contains(tab, permission, tab_permissions):
    """Returns True if the given tab contains the specified permission, otherwise False."""
    if tab in tab_permissions:
        return permission in tab_permissions[tab]
    return False

def getAll(tab, tab_permissions):
    """Returns a list of all permissions associated with the given tab."""
    if tab in tab_permissions:
        return tab_permissions[tab]
    return []

def remove(tab, permission, tab_permissions):
    """Removes the specified permission from the given tab."""
    if tab in tab_permissions and permission in tab_permissions[tab]:
        tab_permissions[tab].remove(permission)

def request(tab, permission, tab_permissions):
    """Adds the specified permission to the given tab."""
    if tab not in tab_permissions:
        tab_permissions[tab] = [permission]
    else:
        tab_permissions[tab].append(permission)