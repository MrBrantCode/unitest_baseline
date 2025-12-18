"""
QUESTION:
Implement a `select_all_rows` function that allows a user to select all rows (not just those currently displayed) from a large dataset (10,000 rows) without loading all data into the client browser. The function should maintain user-specific row selections to prevent interference between users. The solution must be implemented server-side using Spring Boot and MongoDB, and should not store selection state solely in client-side cookies or sessions.
"""

def select_all_rows(user_id, select_all):
    # This function will set or remove the select all flag for a given user
    # Here we're using a dictionary to simulate a database or backend storage
    # In a real application, you would replace this with a database query
    
    # Initialize the user's selection state if it doesn't exist
    if user_id not in user_selections:
        user_selections[user_id] = {'select_all': False}
    
    # Update the user's selection state
    user_selections[user_id]['select_all'] = select_all
    return user_selections[user_id]['select_all']