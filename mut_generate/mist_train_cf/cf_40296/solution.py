"""
QUESTION:
Write a Python function called `extract_and_manipulate_env_vars` that takes a list of environment variable strings and a keyword as input. The function should extract the values of environment variables that contain the keyword and perform a specific operation based on the keyword provided. The environment variable strings are in the format "export VARIABLE_NAME="VALUE"".

The function should handle the keyword "PWD" by returning the longest path among the extracted values, and the keyword "PYTHONPATH" by returning the total count of paths in all the extracted values. If the keyword is not "PWD" or "PYTHONPATH", or if the keyword is not found in any environment variable, the function should return None.
"""

import re

def extract_and_manipulate_env_vars(env_vars, keyword):
    extracted_values = []
    for env_var in env_vars:
        match = re.match(r'export\s+{}\s*=\s*"([^"]+)"'.format(keyword), env_var)
        if match:
            extracted_values.append(match.group(1))

    if keyword == "PWD":
        longest_path = max(extracted_values, key=len, default=None)
        return longest_path
    elif keyword == "PYTHONPATH":
        total_paths = sum(len(path.split(':')) for path in extracted_values)
        return total_paths
    else:
        return None  # Keyword not found