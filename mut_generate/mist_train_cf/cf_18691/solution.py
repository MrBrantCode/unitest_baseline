"""
QUESTION:
Create a function called `create_json_object` that takes a dictionary representing a collection of books categorized by genre, each containing a list of characters, tags, and readers with ratings, and returns a JSON object representing this structure.

The input dictionary should have the following format:
- The keys are the genres of books.
- The values are lists of dictionaries, each representing a book with the following keys: 'id', 'title', 'author', 'publication_year', 'characters', 'tags', and 'readers'.
- The 'characters' and 'tags' are lists of strings.
- The 'readers' is a list of dictionaries, each with 'name' and 'rating'.

The function should return a JSON object with the same structure as the input dictionary, but in JSON format.
"""

import json

def create_json_object(books):
    """
    Convert a dictionary of books categorized by genre into a JSON object.

    Args:
    books (dict): A dictionary where keys are genres and values are lists of dictionaries representing books.

    Returns:
    str: A JSON object representing the input dictionary.
    """
    return json.dumps(books, indent=4)