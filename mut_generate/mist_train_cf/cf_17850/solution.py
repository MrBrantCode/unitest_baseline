"""
QUESTION:
Write a function called `truncate_string` that takes a string and a limit as input. The function should truncate the string after the specified limit and append an ellipsis (...) if the string is longer than the limit. If the limit is less than 1, the function should return an error message. The function should handle both uppercase and lowercase letters, ignore leading and trailing spaces when counting the number of characters, and handle special characters and numbers.
"""

def truncate_string(string, limit):
    if not isinstance(limit, int) or limit < 1:
        return "Error: Invalid limit"
    
    string = string.strip()
    if len(string) <= limit:
        return string
    else:
        return string[:limit] + "..."