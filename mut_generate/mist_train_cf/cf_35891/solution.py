"""
QUESTION:
Generate a unique project name from a given string. The input string should be transformed by converting it to lowercase, replacing all spaces with underscores, and truncating it to 20 characters if it's longer. If the resulting name is already in use, append a sequential number to make it unique.

Write a function `generate_project_name(input_string, existing_project_names)` that takes an input string and a list of existing project names, and returns the unique project name.
"""

from typing import List

def generate_project_name(input_string: str, existing_project_names: List[str]) -> str:
    project_name = input_string.lower().replace(' ', '_')  # Convert to lowercase and replace spaces with underscores
    if len(project_name) > 20:
        project_name = project_name[:20]  # Truncate to 20 characters if longer
    unique_name = project_name
    count = 1
    while unique_name in existing_project_names:
        unique_name = f"{project_name}_{count}"  # Append sequential number if name already exists
        count += 1
    return unique_name