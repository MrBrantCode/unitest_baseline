"""
QUESTION:
Design a function `check_permission(user_role, requested_page)` that determines whether a user has permission to access a requested page based on their role. The function should take two parameters: `user_role` (the user's role) and `requested_page` (the requested page). The function should return `True` if the user has permission and `False` otherwise. The roles and their corresponding permitted pages are defined as follows:
- `roles = {'admin': ['role_detail', 'user_management', 'settings'], 'manager': ['role_detail', 'user_management'], 'user': ['role_detail']}`. 

Note: The `roles` dictionary should be included within the function or be accessible by the function.
"""

def entrance(user_role, requested_page):
    roles = {
        'admin': ['role_detail', 'user_management', 'settings'],
        'manager': ['role_detail', 'user_management'],
        'user': ['role_detail']
    }
    return user_role in roles and requested_page in roles[user_role]