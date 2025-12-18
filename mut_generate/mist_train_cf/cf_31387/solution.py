"""
QUESTION:
Implement a method `check_permission` that checks if a given user has the required permissions for a specific address. The method should take three parameters: `user` (string), `address` (string), and `required_permissions` (list of strings). It should return `True` if the user has all the required permissions for the given address and `False` otherwise. The permissions are stored in the `permissions` dictionary where the keys are user names and the values are dictionaries with addresses as keys and lists of permissions as values. The method should handle cases where the user or address is not found in the `permissions` dictionary.
"""

def check_permission(user, address, required_permissions, permissions):
    """
    Checks if a given user has the required permissions for a specific address.

    Args:
        user (string): The user name.
        address (string): The address.
        required_permissions (list of strings): The required permissions.
        permissions (dictionary): The dictionary containing user permissions.

    Returns:
        boolean: True if the user has all the required permissions, False otherwise.
    """
    user_permissions = permissions.get(user, {})
    address_permissions = user_permissions.get(address, [])
    
    for permission in required_permissions:
        if permission not in address_permissions:
            return False
        
    return True