"""
QUESTION:
Write a function called `consolidate_commits` that takes in a list of commit messages and returns a single commit message that combines all the individual messages. The function should be able to handle an empty list of commit messages. The function should be implemented in Python.

Restrictions: Do not use any external libraries or Git commands.
"""

def consolidate_commits(commit_messages):
    """
    This function consolidates a list of commit messages into a single commit message.
    
    Args:
        commit_messages (list): A list of commit messages.
    
    Returns:
        str: A single commit message combining all individual messages.
    """
    
    # Check if the list is empty
    if not commit_messages:
        return ""
    
    # Use the join function to combine all commit messages into a single string
    # with each message separated by a newline character
    consolidated_message = "\n".join(commit_messages)
    
    return consolidated_message