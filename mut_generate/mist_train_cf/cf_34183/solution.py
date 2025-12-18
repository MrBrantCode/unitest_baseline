"""
QUESTION:
Create a function named `create_post` that takes three parameters: `body`, `author`, and `json_metadata`, and returns a string. The `body` and `author` are strings with a maximum length of 1000 characters, and `json_metadata` is a dictionary representing a valid JSON object. The function should return a message indicating the status of the post creation, which can be "Post created successfully.", "Invalid input: Body cannot be empty.", "Invalid input: Author cannot be empty.", or "Invalid input: Invalid JSON metadata format."
"""

import json

def create_post(body: str, author: str, json_metadata: dict) -> str:
    if not body:
        return "Invalid input: Body cannot be empty."
    if not author:
        return "Invalid input: Author cannot be empty."
    try:
        # Attempt to serialize the JSON metadata to ensure it's valid
        json.dumps(json_metadata)
    except ValueError:
        return "Invalid input: Invalid JSON metadata format."
    
    # Logic to create the post in the social media platform
    # (This part would be specific to the platform's API or database operations)
    
    return "Post created successfully."