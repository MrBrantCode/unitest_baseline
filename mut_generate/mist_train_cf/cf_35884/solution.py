"""
QUESTION:
Write a function `extract_shell_script_params(script: str, params: List[str]) -> Dict[str, str]` that takes a string `script` representing a shell script and a list of parameter names `params` as input, and returns a dictionary where the keys are the parameter names and the values are the assigned values in the script. The script contains valid shell variable assignments and comments, and the parameter names provided will exist in the script. The parameter names are case-sensitive, and the values assigned to the parameters may include spaces and special characters.
"""

from typing import List, Dict

def extract_shell_script_params(script: str, params: List[str]) -> Dict[str, str]:
    param_values = {}
    lines = script.split('\n')
    for line in lines:
        line = line.strip()
        if line and not line.startswith('#'):
            for param in params:
                if line.startswith(param + '='):
                    value = line.split('=')[1].strip()
                    if value.startswith('"') and value.endswith('"'):
                        value = value[1:-1]  # Remove surrounding quotes
                    param_values[param] = value
    return param_values