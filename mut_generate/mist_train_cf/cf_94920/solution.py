"""
QUESTION:
Write a function named `detect_python_version` that takes a Python script as a string input. The function should determine the version of Python the script is compatible with based on its contents and return the version number as a string. The input script may contain syntax errors or unsupported features in certain Python versions, and the function should not execute the script to determine compatibility.
"""

import re

def detect_python_version(script):
    patterns = [
        r"sys\.version_info\s*>=\s*\(\s*(\d+)\s*,\s*(\d+)\s*\)",
        r"sys\.version_info\s*>\s*\(\s*(\d+)\s*,\s*(\d+)\s*\)"
    ]

    for pattern in patterns:
        match = re.search(pattern, script)
        if match:
            major = int(match.group(1))
            minor = int(match.group(2))
            return f"Python {major}.{minor} or higher required"

    return "Python version not supported"