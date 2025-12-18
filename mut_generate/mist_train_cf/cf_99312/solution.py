"""
QUESTION:
Create a function `is_british_hipster_username` that takes a string as input and returns `True` if the string is a valid British hipster username, and `False` otherwise. A valid British hipster username starts with "hip" and ends with "ster", and contains at least one of the following words: "tea", "vinyl", "beard", "tweed", "glasses", or "vegan".
"""

import re

def is_british_hipster_username(username):
    """
    Checks if the given username is a valid British hipster username.
    
    A valid British hipster username starts with "hip" and ends with "ster", 
    and contains at least one of the following words: "tea", "vinyl", "beard", "tweed", "glasses", or "vegan".
    
    Parameters:
    username (str): The username to check.
    
    Returns:
    bool: True if the username is a valid British hipster username, False otherwise.
    """
    pattern = r"^hip(.*)(tea|vinyl|beard|tweed|glasses|vegan)ster$"
    return bool(re.search(pattern, username))