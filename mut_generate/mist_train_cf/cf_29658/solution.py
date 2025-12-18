"""
QUESTION:
Write a function `get_user_permissions(role)` that takes a string `role` as input. The function returns a dictionary containing the permissions for the given role with the following logic: 
- 'mayReadItems', 'mayAddItems', 'mayRemoveItems', 'maySetSeen', 'maySetKeywords', and 'maySubmit' are always True.
- 'mayCreateChild' is always True.
- 'mayRename' and 'mayDelete' are False if the role is truthy, and True otherwise.
"""

def get_user_permissions(role):
    return {
        'mayReadItems': True,
        'mayAddItems': True,
        'mayRemoveItems': True,
        'maySetSeen': True,
        'maySetKeywords': True,
        'mayCreateChild': True,
        'mayRename': not role,
        'mayDelete': not role,
        'maySubmit': True,
    }