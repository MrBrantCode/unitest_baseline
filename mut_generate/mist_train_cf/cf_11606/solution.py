"""
QUESTION:
Create a function `convert_to_json` that takes a nested dictionary as input and returns a JSON object. The dictionary contains a list of books, each with its own unique identifier, title, author, publication year, and tags. The books are categorized into different genres. The JSON object should accurately represent this nested dictionary structure, including the genre and tags for each book.
"""

import json

def convert_to_json(books_dict):
    return json.dumps(books_dict, indent=4)