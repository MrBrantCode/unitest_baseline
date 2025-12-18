"""
QUESTION:
Create a function called `validate_response` that takes a dictionary `response` as input and returns True if the response is successful, and False otherwise. A successful response is defined as having a key "success" with a value of True. The function should return False if the key "success" is not present in the dictionary.
"""

def validate_response(response: dict) -> bool:
    return response.get("success", False)