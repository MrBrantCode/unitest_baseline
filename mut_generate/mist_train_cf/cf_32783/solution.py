"""
QUESTION:
Create a function named `calculate_total_stars` that takes a string representing a TypeScript file snippet as input, extracts the number of GitHub stars associated with each module, and returns the total number of GitHub stars for all the modules. The function should assume that the TypeScript file snippet follows a specific format, where the number of GitHub stars for the entire file is indicated by the `<gh_stars>` tag, and each exported module is preceded by the number of GitHub stars it has. The number of GitHub stars for each module is a non-negative integer.
"""

import re

def calculate_total_stars(typescript_snippet):
    stars_pattern = r'\d+(?=</gh_stars>)'
    module_pattern = r'\d+(?=\s*export \* from)'

    total_stars = 0

    # Extract total stars for the TypeScript file
    total_stars_match = re.search(stars_pattern, typescript_snippet)
    if total_stars_match:
        total_stars = int(total_stars_match.group(0))

    # Extract stars for each module and calculate total stars
    module_matches = re.findall(module_pattern, typescript_snippet)
    for module in module_matches:
        total_stars += int(module)

    return total_stars