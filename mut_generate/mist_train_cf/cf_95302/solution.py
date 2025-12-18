"""
QUESTION:
Create a function called `convert_to_json` that takes a dictionary representing a collection of books as input. The dictionary should have the following structure: the keys are the book genres (e.g., fiction, non-fiction, science fiction), and the values are lists of dictionaries representing individual books. Each book dictionary should contain the keys `id`, `title`, `author`, `publication_year`, `characters`, `tags`, and `readers`. The `characters` and `tags` values should be lists of strings, and the `readers` value should be a list of dictionaries with `name` and `rating` keys. The function should return a JSON string representing the input dictionary.

The function should not take any other parameters, and it should not have any side effects (e.g., it should not print the JSON string). It should also be able to handle dictionaries with any number of genres and books.
"""

import json

def convert_to_json(books):
    return json.dumps(books, indent=4)