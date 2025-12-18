"""
QUESTION:
Write a function `extract_script_info(script)` that takes a string `script` as input and returns a dictionary containing the extracted information. The input `script` represents the content of a script file. The function should extract the following information: 

- The name of the backup folder.
- The list of features choices labels.
- The list of models names.
- The list of normalization choices.

Assumptions: 
- The input `script` is a multi-line string containing commented-out lines starting with `##` and containing the relevant information in the format `## variable_name = 'value'` or `## variable_name = ["value1", "value2", ...]`.
- The commented-out lines may appear in any order within the script.
- The function should return the extracted information as a dictionary with the variable names as keys and the corresponding values.
"""

import re

def extract_script_info(script):
    info = {}
    lines = script.split('\n')
    for line in lines:
        if line.startswith('##'):
            match = re.match(r'##\s*(\w+)\s*=\s*(.*)', line)
            if match:
                key = match.group(1)
                value = match.group(2).strip()
                if value.startswith('[') and value.endswith(']'):
                    value = value[1:-1].replace('"', '').split(',')
                    value = [v.strip() for v in value]
                else:
                    value = value.replace("'", "")
                info[key] = value
    return info