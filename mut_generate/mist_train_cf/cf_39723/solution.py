"""
QUESTION:
Write a function `parse_package_directories(config_file: str) -> dict` that takes a string representing a configuration file where each line maps a package name to its associated directories. The package name and directories are separated by '=>'. The directories are separated by spaces and may contain wildcard characters. The function should return a dictionary where the keys are the package names and the values are lists of directories associated with each package. The function should ignore empty lines in the configuration file and remove any leading or trailing quotes from the package names and directories.
"""

import re

def parse_package_directories(config_file: str) -> dict:
    package_directories = {}
    lines = config_file.split('\n')
    for line in lines:
        if line.strip():  # Check if the line is not empty
            package, directories = line.split('=>')
            package_name = package.strip().strip("'")
            directories = directories.strip().strip().strip("'").strip()
            directories_list = re.split(r'\s+', directories)
            package_directories[package_name] = directories_list
    return package_directories