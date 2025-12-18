"""
QUESTION:
Write a function `json_to_html` that takes a JSON string where keys are integers and values are strings, and returns an HTML unordered list of the corresponding values. The list should be ordered by the keys. The function should not include any error handling.
"""

import json

def json_to_html(json_data):
    data = json.loads(json_data)
    keys = sorted(data.keys(), key=int)
    html_list = "<ul>"
    for key in keys:
        html_list += "<li>" + data[key] + "</li>"
    html_list += "</ul>"
    return html_list