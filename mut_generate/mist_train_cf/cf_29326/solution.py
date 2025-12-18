"""
QUESTION:
Write a function called `generate_info_message(creator_name)` that takes a string `creator_name` as input and returns a message in the format "Made by <creator_name>. All Rights Reserved® <creator_name> :)". The function should replace `<creator_name>` with the actual creator's name provided as input.
"""

def generate_info_message(creator_name):
    return f"Made by {creator_name}. All Rights Reserved {creator_name} :)"