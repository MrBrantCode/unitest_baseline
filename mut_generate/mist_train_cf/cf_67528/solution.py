"""
QUESTION:
Implement a function named `get_username_from_session_id` that retrieves the username associated with a given session ID. The function should accept a session ID as input and return the corresponding username. The function should be designed to work with a custom session state store provider, as the default InProc session store does not allow access to sessions of other users. The solution should also address potential security concerns related to accessing sessions of other users.
"""

def get_username_from_session_id(session_id, session_store):
    """
    Retrieves the username associated with a given session ID.
    
    Args:
        session_id (str): The ID of the session.
        session_store (dict or custom session store): A dictionary or custom session store containing session data.
    
    Returns:
        str: The username associated with the session ID, or None if not found.
    """
    # Assuming session_store is a dictionary where keys are session IDs and values are dictionaries containing user data
    session_data = session_store.get(session_id)
    
    if session_data:
        return session_data.get('username')
    else:
        return None