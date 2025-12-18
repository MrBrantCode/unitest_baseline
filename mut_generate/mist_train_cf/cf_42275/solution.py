"""
QUESTION:
Implement a function `update_user_info(item, **kwargs)` that updates user information based on the provided keyword arguments. The function should take an existing user item and a set of keyword arguments, and return a dictionary containing the updated user information.

The function should accept a dictionary `item` with keys "id", "username", "email", and "date_joined" and keyword arguments `kwargs` representing the fields to be updated. If a keyword argument is not provided, the function should retain the original user information for that field.
"""

def update_user_info(item, **kwargs):
    updated_info = {
        "id": kwargs.get("id", item["id"]),
        "username": kwargs.get("username", item["username"]),
        "email": kwargs.get("email", item["email"]),
        "date_joined": kwargs.get("date_joined", item["date_joined"]),
    }
    return updated_info