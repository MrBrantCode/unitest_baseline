"""
QUESTION:
Create a function `generate_british_hipster_username` that generates a username using regular expressions. The username must start with "hip" and end with "ster", and contain at least one of the following words: "tea", "vinyl", "beard", "tweed", "glasses", or "vegan".
"""

import re

def generate_british_hipster_username(username):
    pattern = r"^hip(.*)(tea|vinyl|beard|tweed|glasses|vegan)ster$"
    match = re.search(pattern, username)
    if match:
        return match.group(0)
    else:
        return "No match found."