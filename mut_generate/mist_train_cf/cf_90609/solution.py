"""
QUESTION:
Implement a function `validate_branch_name(branch_name)` that takes a string `branch_name` as input and returns a boolean value indicating whether the name is valid or not. The `branch_name` must follow the format "feature/<feature-name>/<your-initials>", where `<feature-name>` starts with a lowercase letter and consists of only alphanumeric characters and underscores, and `<your-initials>` consists of exactly two uppercase letters. The `branch_name` should not exceed 50 characters. The function should handle edge cases such as an empty string or a branch name that does not contain the necessary components.
"""

import re

def validate_branch_name(branch_name):
    # Check if the branch name is empty or exceeds 50 characters
    if not branch_name or len(branch_name) > 50:
        return False
    
    # Validate the branch name format
    pattern = r'^feature/[a-z][a-z0-9_]+/[A-Z]{2}$'
    if not re.match(pattern, branch_name):
        return False
    
    return True