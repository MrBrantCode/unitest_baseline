"""
QUESTION:
Write a Python function `extract_env_vars(config_file)` that takes a string `config_file` representing the content of a configuration file. The function should extract environment variable assignments from `config_file` in the format `VARIABLE_NAME=value` and return them as a list of strings. The configuration file can contain comments denoted by the `#` character at the beginning of a line or after a variable assignment, which should be ignored.
"""

import re

def extract_env_vars(config_file):
    env_vars = []
    lines = config_file.split('\n')
    for line in lines:
        line = line.strip()
        if line and not line.startswith('#'):
            match = re.match(r'^([^#]+)', line)
            if match:
                env_vars.append(match.group(1).strip())
    return env_vars