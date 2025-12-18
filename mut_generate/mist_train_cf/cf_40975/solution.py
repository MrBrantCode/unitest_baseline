"""
QUESTION:
Implement the `sanitize_user_agent(user_agent: str) -> str` function. It should take a user-agent string as input and return a sanitized version of the string, removing any potentially harmful characters or code that could lead to code injection attacks. The function should replace semicolons, backticks, single quotes, and double quotes with an empty string to prevent code injection attacks.
"""

import re

def sanitize_user_agent(user_agent: str) -> str:
    # Define a regular expression pattern to match potentially harmful characters
    pattern = r'[;`\'"]'

    # Use the sub() function from the re module to replace potentially harmful characters with an empty string
    sanitized_user_agent = re.sub(pattern, '', user_agent)

    return sanitized_user_agent