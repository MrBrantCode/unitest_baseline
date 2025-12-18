"""
QUESTION:
Implement a function `validateApiKey` that takes a string `api_key` as input. The function should validate the API key based on the following rules: 
- The API key must contain the string "Type = \"apiKey\";".
- The API key must be at least 10 characters long.
- The API key must contain at least one uppercase letter, one lowercase letter, and one digit.
The function should return `True` if the API key is valid and `False` otherwise.
"""

def validateApiKey(api_key):
    if len(api_key) < 10:
        return False
    if "Type = \"apiKey\";" not in api_key:
        return False
    if not any(char.isupper() for char in api_key):
        return False
    if not any(char.islower() for char in api_key):
        return False
    if not any(char.isdigit() for char in api_key):
        return False
    return True