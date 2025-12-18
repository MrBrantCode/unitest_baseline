"""
QUESTION:
Create a function `parse_comments` that takes a list of rows from a database table 'Users' with a column 'Comments' containing JSON strings as input. The function should parse the JSON strings, extract the values for the keys 'name' and 'email' for each comment, discard comments with invalid email formats, and return a list of the extracted values sorted in alphabetical order based on the 'name' key. 

The input rows are expected to have a single column 'Comments', and the JSON strings in this column contain lists of comments where each comment is a dictionary with 'name' and 'email' keys. A valid email format is considered to be any string that matches the regular expression `[^@]+@[^@]+\.[^@]+`.
"""

import json
import re

def parse_comments(rows):
    """
    Parse JSON strings in the 'Comments' column of the input rows, extract the values 
    for the keys 'name' and 'email' for each comment, discard comments with invalid 
    email formats, and return a list of the extracted values sorted in alphabetical 
    order based on the 'name' key.

    Args:
        rows (list): A list of rows from a database table 'Users' with a column 
            'Comments' containing JSON strings.

    Returns:
        list: A list of dictionaries containing 'name' and 'email' values for valid comments.
    """
    valid_comments = []

    for row in rows:
        comments_json = row[0]
        comments = json.loads(comments_json)

        for comment in comments:
            name = comment.get('name')
            email = comment.get('email')

            if email is not None and re.match(r"[^@]+@[^@]+\.[^@]+", email):
                valid_comments.append({'name': name, 'email': email})

    valid_comments.sort(key=lambda x: x['name'])
    return valid_comments