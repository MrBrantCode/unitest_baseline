"""
QUESTION:
Create a function named `manage_conversation_state` that keeps track of the conversation context in a chatbot conversation. The function should store the conversation ID and the current state in a database. The state should be updated based on the user's response to a list of options. The function should be able to handle multiple conversation branches and update the state accordingly.
"""

def manage_conversation_state(conversation_id, user_response, database, states, current_state):
    """
    Manage the conversation state in a chatbot conversation.

    Args:
    conversation_id (str): The unique ID of the conversation.
    user_response (str): The user's response to the current state.
    database (dict): A dictionary representing the database to store conversation states.
    states (dict): A dictionary mapping states to their corresponding next states based on user responses.
    current_state (str): The current state of the conversation.

    Returns:
    str: The updated state of the conversation.
    """

    # Check if the conversation ID exists in the database
    if conversation_id not in database:
        database[conversation_id] = current_state

    # Update the state based on the user's response
    if user_response in states[current_state]:
        database[conversation_id] = states[current_state][user_response]

    return database[conversation_id]