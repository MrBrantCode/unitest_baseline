"""
QUESTION:
Write a function named `get_database_path` that returns the database path required for specifying security rules in Google Firestore, considering that each project can have only one database.
"""

def get_database_path(project_id, database_id='(default)'):
    """
    Returns the database path required for specifying security rules in Google Firestore.

    Args:
        project_id (str): The ID of the Firebase project.
        database_id (str): The ID of the Firestore database. Defaults to '(default)'.

    Returns:
        str: The database path in the format '/databases/{database}/documents'.
    """
    return f'/databases/{database_id}/documents'