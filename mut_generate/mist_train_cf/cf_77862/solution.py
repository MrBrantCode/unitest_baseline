"""
QUESTION:
Write a function `process_json(data)` to construct an HTML nested list from a recursively nested JSON object. The function should handle erroneous entries that do not follow the pattern by ignoring them. 

The input JSON object has two possible valid formats: 
1. A dictionary containing 'listTitle' and 'listItems', where 'listItems' is a list of either strings or dictionaries with the same structure.
2. A string representing a list item.

The output should be a string representing an HTML nested list.
"""

def process_json(data):
    if isinstance(data, dict) and 'listTitle' in data and 'listItems' in data:
        return f'<h2>{data["listTitle"]}</h2>\n<ul>{"".join(map(process_json, data["listItems"]))}</ul>\n'
    elif isinstance(data, str):
        return f'<li>{data}</li>\n'
    else:
        return ''  # Ignore invalid data