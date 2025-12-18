"""
QUESTION:
Create a function `add_user_to_group(username: str, groupname: str) -> str` that simulates adding a user to a group and returns a string indicating the success or failure of the operation. The function should check if the group exists and if the user is already a member of the group. If the group does not exist, the function should return a message indicating so. If the user is already a member of the group, the function should return a message indicating that the user is already a member. Otherwise, the function should add the user to the group and return a success message. Assume that the group information is available and can be used within the function.
"""

def add_user_to_group(username: str, groupname: str, groups: dict) -> str:
    """
    Simulates adding a user to a group and returns a string indicating the success or failure of the operation.

    Args:
        username (str): The username to be added to the group.
        groupname (str): The name of the group to which the user is to be added.
        groups (dict): A dictionary containing group information.

    Returns:
        str: A message indicating the success or failure of the operation.
    """
    if groupname in groups:
        if username in groups[groupname]:
            return f"User '{username}' is already a member of group '{groupname}'."
        else:
            groups[groupname].append(username)
            return f"User '{username}' added to group '{groupname}' successfully."
    else:
        return f"Group '{groupname}' does not exist."