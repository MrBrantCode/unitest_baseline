"""
QUESTION:
Create a function named `remove_team_member` that restricts a team member's access to a repository. The function should not attempt to delete the member's local clone, as this is not possible. Instead, it should focus on removing the member's push and pull permissions.
"""

def remove_team_member(team_members, member_to_remove):
    """
    Removes a team member's push and pull permissions.

    Args:
        team_members (list): A list of current team members.
        member_to_remove (str): The name of the team member to be removed.

    Returns:
        list: The updated list of team members after removal.
    """
    if member_to_remove in team_members:
        team_members.remove(member_to_remove)
    return team_members