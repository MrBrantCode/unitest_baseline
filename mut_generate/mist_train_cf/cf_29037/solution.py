"""
QUESTION:
Write a function `process_modification_commands(commands: List[str]) -> Tuple[Dict[int, int], str]` that takes in a list of file modification commands where each command is a string in the format `<filename><gh_stars>1-10` followed by a `chgrp` command. The function should return a tuple containing: 
1. A dictionary where the keys are severity levels (the first number in the `<gh_stars>1-10` range) and the values are the total number of modifications required for each severity level.
2. The filename of the file with the highest severity modification (the second number in the `<gh_stars>1-10` range). The input list has a length that is a multiple of 2, with each pair of elements containing the filename with severity range and the corresponding `chgrp` command. The function should process the list in steps of 2, ignoring the `chgrp` commands.
"""

from typing import List, Tuple, Dict

def process_modification_commands(commands: List[str]) -> Tuple[Dict[int, int], str]:
    severity_modifications = {}
    max_severity_file = ("", 0)

    for i in range(0, len(commands), 2):
        filename, severity = commands[i].split("<gh_stars>")
        severity_range = list(map(int, severity.split("-")))
        severity_level = severity_range[0]
        if severity_level not in severity_modifications:
            severity_modifications[severity_level] = 1
        else:
            severity_modifications[severity_level] += 1

        if severity_range[1] > max_severity_file[1]:
            max_severity_file = (filename, severity_range[1])

    return severity_modifications, max_severity_file[0]