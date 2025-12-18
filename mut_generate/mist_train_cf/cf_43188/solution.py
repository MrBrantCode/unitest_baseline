"""
QUESTION:
Implement the `delete` method in the `ActivityManager` class. This method should take a `pk` (primary key) as input and delete the activity area with the given ID if the following conditions are met: 
- The requesting user is an admin. 
- The activity area with the given ID exists and its status is active (True). 
If the deletion is successful, return a status code of 204 with a message. If the activity area does not exist, return a message with a status code of 204. If the requesting user is not an admin, return an error message with a status code of 400.
"""

def delete(pk, user, activities):
    """
    Deletes an activity area with the given ID if the requesting user is an admin and the activity area exists and is active.

    Args:
    pk (int): The primary key of the activity area to delete.
    user (dict): The requesting user with 'is_admin' status.
    activities (list): A list of activity areas.

    Returns:
    tuple: A status code and a message.
    """

    # Check if the requesting user is an admin
    if not user['is_admin']:
        return 400, "Only admins can delete activity areas."

    # Find the activity area with the given ID
    activity = next((a for a in activities if a['id'] == pk), None)

    # Check if the activity area exists and is active
    if activity is None or not activity['is_active']:
        return 404, "Activity area not found."

    # Update the status of the activity area to inactive (simulating deletion)
    activity['is_active'] = False

    return 204, "Activity area deleted successfully."