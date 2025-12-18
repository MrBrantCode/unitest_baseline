"""
QUESTION:
Implement the function `is_valid_git_branch(branch_name: str) -> bool` that checks if a given string is a valid Git branch name. A valid Git branch name must not contain any whitespace characters, the characters `~^:?*[\`, start with a hyphen (`-`), end with a forward slash (`/`), contain two consecutive dots (`..`), or contain a sequence of a dot followed by a forward slash (`./`). The function should return `True` if the input string is a valid Git branch name and `False` otherwise.
"""

import re

def is_valid_git_branch(branch_name: str) -> bool:
    if any(char in branch_name for char in ['~', '^', ':', '?', '*', '[', '\\']) or \
       ' ' in branch_name or \
       branch_name.startswith('-') or \
       branch_name.endswith('/') or \
       '..' in branch_name or \
       './' in branch_name:
        return False
    return True