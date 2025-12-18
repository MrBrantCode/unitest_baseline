"""
QUESTION:
Write a function `parse_dependencies(config_file)` that takes a configuration file as input, parses it, and returns a dictionary containing the extracted information for each dependency. The configuration file contains function calls like `http_archive` and `go_repository` with specific parameters such as `name`, `urls`, `sha256`, `importpath`, and `sum`. The function should extract these parameters for each dependency and return a dictionary with the dependency name as the key and another dictionary containing the extracted parameters as the value. The function should be able to handle dependencies with different sets of parameters.
"""

import re

def parse_dependencies(config_file):
    dependencies = {}
    pattern = re.compile(r'(\w+)\(\s*name\s*=\s*"(.*?)",\s*urls\s*=\s*(\[.*?\]),?\s*sha256\s*=\s*"(.*?)",?\s*importpath\s*=\s*"(.*?)",?\s*sum\s*=\s*"(.*?)"?\s*\)')

    matches = pattern.findall(config_file)
    for match in matches:
        dependency = match[0]
        info = {}
        if match[1]:
            info["name"] = match[1]
        if match[2]:
            info["urls"] = eval(match[2])
        if match[3]:
            info["sha256"] = match[3]
        if match[4]:
            info["importpath"] = match[4]
        if match[5]:
            info["sum"] = match[5]
        dependencies[dependency] = info

    return dependencies