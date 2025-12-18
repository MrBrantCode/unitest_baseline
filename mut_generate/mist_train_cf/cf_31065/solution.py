"""
QUESTION:
Implement a function `parse_code_snippet(code: str) -> (int, str)` that takes a string `code` containing a code snippet as input and returns a tuple containing the number of GitHub stars (an integer) and the coding language used in the project (a string). The code snippet follows the format where the number of GitHub stars is indicated by the `<gh_stars>` tag and the coding language is specified in the comment block following the encoding declaration.
"""

import re

def parse_code_snippet(code: str) -> (int, str):
    stars_pattern = r'<gh_stars>(\d{1,2})'
    language_pattern = r'# -\*- coding: ([a-zA-Z0-9-]+) -\*-'

    stars_match = re.search(stars_pattern, code)
    language_match = re.search(language_pattern, code)

    if stars_match and language_match:
        stars = int(stars_match.group(1))
        language = language_match.group(1)
        return stars, language
    else:
        return None, None  # Handle case when patterns are not found