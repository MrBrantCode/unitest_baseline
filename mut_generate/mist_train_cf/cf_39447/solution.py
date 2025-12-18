"""
QUESTION:
Write a function `parse_environment_variables(env_string: str) -> List[str]` that takes in a string `env_string` representing environment variable assignments in the format of shell commands and returns a list of individual paths extracted from the `PATH` and `ROS_PACKAGE_PATH` variables. The string is expected to contain multiple lines, with each line representing an environment variable assignment in the form of `export VARIABLE_NAME="value"`.
"""

from typing import List

def parse_environment_variables(env_string: str) -> List[str]:
    paths = []
    lines = env_string.split('\n')
    for line in lines:
        if line.startswith('export PATH='):
            path_value = line.split('export PATH=')[1].strip('"')
            paths.extend(path_value.split(':'))
        elif line.startswith('export ROS_PACKAGE_PATH='):
            ros_path_value = line.split('export ROS_PACKAGE_PATH=')[1].strip('"').split(':')
            paths.extend(ros_path_value)
    return paths