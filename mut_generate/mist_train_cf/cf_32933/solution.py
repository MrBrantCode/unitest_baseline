"""
QUESTION:
Implement a `filter_payload` function that takes a dictionary as input and returns a new dictionary with non-essential or sensitive data filtered out. The function should remove any key-value pairs where the value is `None`. Additionally, implement a `delete_user` method in the `DatabaseManager` class that takes a `user_id` as input and deletes the corresponding user from the database.
"""

import typing

def filter_payload(payload: dict) -> dict:
    # Filter out any non-essential or sensitive data from the payload
    filtered_payload = {k: v for k, v in payload.items() if v is not None}
    return filtered_payload

class DatabaseManager:
    async def delete_user(self, user_id: int) -> None:
        # Delete the user from the database based on the user_id
        # Assume implementation details not provided
        pass