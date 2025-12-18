"""
QUESTION:
Write a function called `isValidURL` that takes a string as input and returns True if it is a valid URL, False otherwise. The input string must start with either "http://" or "https://", contain at least one dot (".") after the prefix, not contain any whitespace characters, and end with a valid top-level domain (e.g., ".com", ".org", ".edu"). The input string will only contain lowercase and uppercase letters, numbers, dots (".") and slashes ("/").
"""

def isValidURL(url):
    prefixes = ["http://", "https://"]
    valid_tlds = [".com", ".org", ".edu"]
    
    if not url.startswith(tuple(prefixes)):
        return False
    
    dot_index = url.find(".", len(prefixes[0]))
    if dot_index == -1:
        return False
    
    if any(char.isspace() for char in url):
        return False
    
    if not url.endswith(tuple(valid_tlds)):
        return False
    
    return True