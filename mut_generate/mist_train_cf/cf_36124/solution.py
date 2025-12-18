"""
QUESTION:
Create a function `determine_home_page(role, user_function)` that takes in a user's role and function, and returns the appropriate home page based on the following rules and configurations:
- If `role` is found in `role_home_page`, return the corresponding home page.
- If `get_home_page(user_function)` is defined, use it to determine the home page based on `user_function`.
- Otherwise, return the default `home_page`. 

Configurations:
- `home_page`: the default home page
- `role_home_page`: a dictionary mapping roles to their respective home pages
- `get_home_page(user_function)`: a function determining the home page based on `user_function`
"""

def determine_home_page(role, user_function, home_page, role_home_page, get_home_page):
    if role in role_home_page:
        return role_home_page[role]
    elif callable(get_home_page) and user_function:
        return get_home_page(user_function)
    else:
        return home_page