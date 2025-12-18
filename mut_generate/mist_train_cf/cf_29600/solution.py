"""
QUESTION:
Create a function `extractRepoInfo` that takes a string representing a GitHub repository URL as input and returns a tuple containing the repository owner's username and the repository name. The input URL will always be in the format "https://github.com/username/repositoryname".
"""

import re

def extractRepoInfo(url):
    pattern = r"https://github.com/(\w+)/(\w+)"
    match = re.match(pattern, url)
    if match:
        return match.group(1), match.group(2)
    else:
        return None