"""
QUESTION:
Implement a function `process_environment_variables` that takes a list of tuples containing environment variable names, file names, and variable types. The function should repeat the file names and the string 'optional' for each optional environment variable and sort the optional environment variables. For non-optional environment variables, repeat the file names and the string 'required'. Return a list of tuples containing the processed environment variable information.
"""

from itertools import repeat

def process_environment_variables(environment_variables):
    """
    Process the list of environment variables and their associated file names.

    Args:
    environment_variables: A list of tuples containing environment variable names, file names, and variable types.

    Returns:
    A list of tuples containing processed environment variable information.
    """
    envvars = []
    for filename, var_type, var_name in environment_variables:
        if var_type == 'optional':
            envvars.extend(list(zip(
                repeat(filename),
                repeat('optional'),
                sorted(var_name)
            )))
        else:
            envvars.extend(list(zip(
                repeat(filename),
                repeat('required'),
                var_name
            )))
    return envvars