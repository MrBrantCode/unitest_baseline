"""
QUESTION:
Write a function called `isValidURL(url)` that checks if a given string is a valid URL. 

The function should return True if the string meets the following conditions:
- It starts with either "http://" or "https://".
- It contains at least one dot (".") after the prefix.
- It does not contain any whitespace characters.
- It ends with a valid top-level domain (e.g., ".com", ".org", ".edu").

Note: The input string will only contain lowercase and uppercase letters, numbers, dots (".") and slashes ("/").
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