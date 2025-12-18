"""
QUESTION:
Create a function named `unset_specific_env_vars` that takes a dictionary of environment variables as input and returns a modified dictionary. The function should remove variables that start with either "LD_" or "TERMUX_". The input dictionary should not be modified in place, and the function should return a new dictionary with the specified variables removed.
"""

def unset_specific_env_vars(env_vars):
    modified_env_vars = env_vars.copy()

    for key in list(modified_env_vars.keys()):
        if key.startswith("LD_") or key.startswith("TERMUX_"):
            del modified_env_vars[key]

    return modified_env_vars