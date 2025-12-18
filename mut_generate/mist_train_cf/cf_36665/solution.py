"""
QUESTION:
Implement a Python function `extract_meas_values(config_file_content: str) -> List[int]` that takes the content of a configuration file as a string. The configuration file contains multiple lines, each representing a different measurement setup in the form of a `calc_run` function call with various parameters passed as keyword arguments. The function should extract the values of the `meas` parameter for each measurement setup and return them as a list of integers. Assume the `meas` parameter is always present, specified as a keyword argument, and its value is an integer.
"""

from typing import List
import re

def extract_meas_values(config_file_content: str) -> List[int]:
    meas_values = []
    pattern = r"meas=(\d+)"
    matches = re.findall(pattern, config_file_content)
    for match in matches:
        meas_values.append(int(match))
    return meas_values