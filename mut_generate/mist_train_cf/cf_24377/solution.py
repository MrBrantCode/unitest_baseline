"""
QUESTION:
Construct a regex pattern to match any 5-digit US zip code. The zip code should consist of exactly 5 digits with no additional characters.
"""

import re

def match_zip_code(zip_code):
    pattern = r'^\d{5}$'
    return bool(re.match(pattern, zip_code))