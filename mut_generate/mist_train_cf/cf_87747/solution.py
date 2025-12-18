"""
QUESTION:
Write a function named `truncate_string` that takes two parameters: `string` and `limit`. The function should return a truncated version of the input string, with ellipsis (...) appended if the string is longer than the specified limit. If the limit is less than or equal to 0, the function should return an error message. The function should handle strings with uppercase and lowercase letters, special characters, and numbers; ignore leading and trailing spaces; and check if the input limit is a valid integer.
"""

def truncate_string(string, limit):
    if not isinstance(limit, int) or limit <= 0:
        return "Error: Invalid limit"
    
    string = string.strip()
    if len(string) <= limit:
        return string
    else:
        return string[:limit] + "..."