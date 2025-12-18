"""
QUESTION:
Write a function `parseReadme` that takes a string `readme` as input and returns a dictionary containing the repository name, author, and description. The repository name and author are extracted from the string in the format `<reponame>username/repositoryname`, and the description is the content within the first set of non-empty double quotes. The function assumes that the input string will always contain the repository name, author, and description in the specified format.
"""

import re

def parseReadme(readme):
    result = {}
    
    # Extract repository name and author
    match = re.search(r'<reponame>(\w+)/(\w+)', readme)
    result["author"] = match.group(1)
    result["repository"] = match.group(2)
    
    # Extract description within double quotes
    description_match = re.search(r'"([^"]+)"', readme)
    result["description"] = description_match.group(1)
    
    return result