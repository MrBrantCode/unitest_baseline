"""
QUESTION:
Write a function `next_upcoming_contest` that takes two parameters: a string `completed_contest` representing the name of a contest that has been completed and a list `upcoming_contests` of upcoming contests. Remove the completed contest from the list and return the name of the next upcoming contest. The list of contests is guaranteed to contain at least two contests, and the completed contest is guaranteed to be present in the list.
"""

def next_upcoming_contest(completed_contest, upcoming_contests):
    """
    Returns the name of the next upcoming contest after removing the completed contest.

    Args:
        completed_contest (str): The name of the completed contest.
        upcoming_contests (list): A list of upcoming contests.

    Returns:
        str: The name of the next upcoming contest.
    """
    upcoming_contests.remove(completed_contest)
    return upcoming_contests[0]