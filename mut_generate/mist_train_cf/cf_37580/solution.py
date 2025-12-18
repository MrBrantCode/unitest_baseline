"""
QUESTION:
Write a Python function `parse_cromwell_command(command)` that takes a string `command` as input and returns a dictionary containing the file paths for the configuration, JAR, inputs, pipeline, and log. The function should handle both absolute and relative file paths. The input `command` string represents a shell command that runs a pipeline using Cromwell, a workflow management system, and contains the file paths as arguments.
"""

import re

def parse_cromwell_command(command):
    file_paths = {}
    pattern = r'(-Dconfig\.file=|jar )([^ ]+)'
    matches = re.findall(pattern, command)
    for match in matches:
        if match[0] == '-Dconfig.file=':
            file_paths["CONFIG"] = match[1]
        else:
            file_paths["JAR"] = match[1]

    pattern = r'run -i ([^ ]+) ([^ ]+)'
    matches = re.search(pattern, command)
    if matches:
        file_paths["INPUTS"] = matches.group(1)
        file_paths["PIPELINE"] = matches.group(2)

    pattern = r'tee ([^ ]+)'
    matches = re.search(pattern, command)
    if matches:
        file_paths["LOG"] = matches.group(1)

    return file_paths