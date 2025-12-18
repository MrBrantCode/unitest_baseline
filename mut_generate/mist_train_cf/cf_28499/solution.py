"""
QUESTION:
Implement the `MetaDataObjectPermissions` class with `has_view_permission(user, metadata_object)` and `has_delete_permission(user, metadata_object)` methods. The `has_view_permission` method should return `True` if the user has permission to view the metadata object, otherwise `False`. The `has_delete_permission` method should return `True` if the user has permission to delete the metadata object, otherwise `False`. Assume that the `metadata_object` passed to the methods is an instance of a metadata object and the `user` is an instance of a user with attributes such as `role` and `metadata_object` has attributes such as `public` and `owner`.
"""

def entance(user, metadata_object):
    # Implement logic to check if the user has view permission for the metadata object
    # Example: Check if the user has the required role or access level
    # Replace the condition with the actual logic based on your permission system
    if user.role == 'admin' or metadata_object.public:
        return True
    return False

def entance_del(user, metadata_object):
    # Implement logic to check if the user has delete permission for the metadata object
    # Example: Check if the user has the required role or ownership of the object
    # Replace the condition with the actual logic based on your permission system
    if user.role == 'admin' or metadata_object.owner == user:
        return True
    return False