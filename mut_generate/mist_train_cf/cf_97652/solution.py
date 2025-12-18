"""
QUESTION:
Create a function called `match_hipster_username` that uses regular expressions to match a username that starts with "hip" and ends with "ster" and contains at least one of the following words: "tea", "vinyl", "beard", "tweed", "glasses", or "vegan". The function should return a match if the username meets the requirements, otherwise it should return "No match found."
"""

import re

def match_hipster_username(username):
    pattern = r"^hip(.*)(tea|vinyl|beard|tweed|glasses|vegan)ster$"
    match = re.search(pattern, username)
    if match:
        return match.group(0)
    else:
        return "No match found."