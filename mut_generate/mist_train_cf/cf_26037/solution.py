"""
QUESTION:
Create a function `format_result` that takes a list of rows from a database query as input. Each row is a tuple containing an `id` and a `value`. The function should return a JSON-formatted list of dictionaries, where each dictionary represents a row with `id` and `value` keys.
"""

import json

def format_result(rows):
    """
    Formats a list of database query rows into a JSON-formatted list of dictionaries.

    Args:
        rows (list): A list of tuples containing an id and a value.

    Returns:
        str: A JSON-formatted list of dictionaries, where each dictionary represents a row with id and value keys.
    """
    json_result = []
    for row in rows:
        row_dict = {
            "id": row[0], 
            "value": row[1]
        }
        json_result.append(row_dict)
    return json.dumps(json_result)