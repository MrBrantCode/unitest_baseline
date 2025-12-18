"""
QUESTION:
Implement a function `can_delete_taxonomy` that takes into account the access control logic for taxonomy deletion. The function should return a boolean value indicating whether a user has the necessary permissions to delete a taxonomy based on the given criteria.

The function should take the following parameters: 
- `user_groups`: A list of groups to which the user belongs.
- `has_classifications`: A boolean indicating whether the taxonomy has any classifications attached.
- `is_shared`: A boolean indicating whether the taxonomy is shared with at least one of the user's groups.
- `is_system_admin`: A boolean indicating whether the user is a system admin.
- `has_delete_taxonomy_acl`: A boolean indicating whether the user has the delete taxonomy ACL.

The function should return `True` if the user has the necessary permissions to delete the taxonomy and `False` otherwise.
"""

def can_delete_taxonomy(user_groups, has_classifications, is_shared, is_system_admin, has_delete_taxonomy_acl):
    if is_system_admin:
        return True
    elif has_delete_taxonomy_acl and not has_classifications:
        return is_shared
    else:
        return False