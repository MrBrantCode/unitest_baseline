"""
QUESTION:
Write a function named `extract_directory_names` that takes a string of file paths separated by a plus sign as input, where each file path is enclosed in double quotes and ends with the "/Headers" directory. The function should return a list of unique directory names extracted from the paths, excluding the "/Headers" directory.
"""

import re
from pathlib import Path

def extract_directory_names(input_string):
    paths = re.findall(r'"(.*?/Headers)"', input_string)
    unique_directories = list(set([Path(path).parent.name for path in paths]))
    return unique_directories