"""
QUESTION:
Create a function named `validate_branch_name` that takes a proposed branch name as input and returns a boolean value indicating whether the name is valid or not. The branch name must follow the format "feature/\<feature-name>/\<your-initials>" where \<feature-name> can contain alphabets, numbers, and hyphens, and \<your-initials> can contain only alphabets. The branch name should not exceed 30 characters.
"""

import re

def validate_branch_name(branch_name):
    # Check if branch name is empty or exceeds 30 characters
    if not branch_name or len(branch_name) > 30:
        return False

    # Define the regex pattern for branch name validation
    pattern = r'^feature/[a-zA-Z0-9-]+/[a-zA-Z]+$'

    # Check if branch name matches the pattern
    if not re.match(pattern, branch_name):
        return False

    return True