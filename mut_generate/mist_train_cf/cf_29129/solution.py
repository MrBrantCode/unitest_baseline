"""
QUESTION:
Extract the value assigned to a specified environment variable in a given shell script. 

Write a function `extract_env_variable_value(script: str, variable_name: str) -> str` that takes a shell script as a string and the name of the environment variable as a string, and returns the value assigned to the specified environment variable. The environment variable assignment is always in the format `export VARIABLE_NAME="value"`.
"""

import re

def extract_env_variable_value(script: str, variable_name: str) -> str:
    pattern = r'export\s' + re.escape(variable_name) + r'="(.*?)"'
    match = re.search(pattern, script)
    if match:
        return match.group(1)
    else:
        return ""