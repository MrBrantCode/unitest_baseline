"""
QUESTION:
Create a function named `validate_branch_name` that takes a proposed branch name as input and returns a boolean value indicating whether the name is valid or not. The branch name should follow the format "feature/\<feature-name>/\<your-initials>", not exceed 50 characters, and adhere to the following naming conventions: 
- The feature-name component should start with a lowercase letter and consist of only alphanumeric characters and underscores.
- The your-initials component should consist of exactly two uppercase letters.
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