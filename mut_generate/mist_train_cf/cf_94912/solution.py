"""
QUESTION:
Write a function named `truncate_string` that truncates a given string after a specified number of characters and returns the truncated string. The function should append ellipsis (...) at the end of the truncated string if the original string is longer than the specified limit. The function should handle both uppercase and lowercase letters, ignore leading and trailing spaces, and handle special characters and numbers. If the string length is less than or equal to the limit, the function should return the original string without any changes. If the input limit is not a valid integer or is less than 1, the function should return an error message.
"""

def truncate_string(string, limit):
    if not isinstance(limit, int) or limit < 1:
        return "Error: Invalid limit"
    
    string = string.strip()
    if len(string) <= limit:
        return string
    else:
        return string[:limit] + "..."