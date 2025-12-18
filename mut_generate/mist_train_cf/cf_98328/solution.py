"""
QUESTION:
Create a function `get_environment_variables` that takes a `user` as input and returns a dictionary of environment variables specific to that user in a Unix-based system. The function should filter environment variables that start with the user name followed by an underscore.
"""

def get_environment_variables(user):
    """
    Returns a dictionary of environment variables specific to the given user in a Unix-based system.

    :param user: The user account name.
    :return: A dictionary of environment variables.
    """
    env_vars = {}
    for key, value in os.environ.items():
        if key.startswith(user + "_"):
            env_vars[key] = value
    return env_vars