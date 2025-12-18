"""
QUESTION:
Implement the `check` method of the `RoleBased` class, which takes a `field` as input and returns a boolean indicating whether the current user has the necessary permissions to access the field. The method should use the `role_perms` dictionary, where keys are roles and values are sets of permissions, to determine the user's permissions based on their role. If the user's role is not found in `role_perms`, default to the permissions associated with the wildcard role '*'. The `field.env.user` attribute provides the current user, and `field.required_permissions` is a set of required permissions for the field.
"""

def check(field, role_perms, user):
    perms = set(role_perms.get('*', ''))  # Retrieve permissions for wildcard role if user's role is not found
    user_perms = role_perms.get(user.role, set())  # Retrieve permissions for user's role

    if user_perms:  # If user's role is found in role_perms
        perms.update(user_perms)  # Update permissions with user's role permissions

    required_perms = field.required_permissions  # Assuming field.required_permissions is a set of required permissions
    return required_perms.issubset(perms)  # Check if user has necessary permissions for the field