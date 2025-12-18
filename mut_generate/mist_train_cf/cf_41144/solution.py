"""
QUESTION:
Implement a `change_room` function that takes a user's chat ID as input and returns a message indicating their new room or a message stating that no change is required. 

The function should have the following signature: `def change_room(chat_id: str) -> str:`

The function should use the provided list of relative chat IDs to determine whether the user's chat ID requires a room change. If a change is required, the function should return a message indicating the user's new room. If no change is required, the function should return a message stating so.
"""

def change_room(chat_id: str, relative_chat_ids: list, new_room: str) -> str:
    """
    This function determines whether a user's chat ID requires a room change and returns a message accordingly.

    Args:
        chat_id (str): The user's chat ID.
        relative_chat_ids (list): A list of relative chat IDs.
        new_room (str): The new room for the user.

    Returns:
        str: A message indicating the user's new room or stating that no change is required.
    """

    # Determine if the user's chat ID requires a room change
    if chat_id in relative_chat_ids:
        # Return a message indicating the user's new room
        return f"Ваша новая комната\n{new_room}"
    else:
        # Return a message stating that no change is required
        return "На данный момент ничего менять не требуется"