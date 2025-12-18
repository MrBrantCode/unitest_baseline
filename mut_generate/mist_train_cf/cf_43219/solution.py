"""
QUESTION:
Define a function `set_environment_variables` that takes a dictionary of environment variables and their default values as input, checks for their presence using `os.environ.get()`, and assigns the default values if they are not present. The function should then return the final values of the environment variables.
"""

import os

def set_environment_variables(env_variables):
    """
    Sets environment variables and assigns default values if not present.

    Args:
    env_variables (dict): Dictionary of environment variables and their default values.

    Returns:
    dict: Dictionary containing the final values of the environment variables.
    """
    for key, value in env_variables.items():
        if os.environ.get(key) is not None:
            env_variables[key] = os.environ.get(key)
    return env_variables