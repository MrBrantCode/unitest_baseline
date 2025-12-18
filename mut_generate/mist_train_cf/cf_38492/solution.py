"""
QUESTION:
Create a function named `extract_button_attributes` that takes a string `html_template` of length 1 to 1000 as input and returns a dictionary. The input string is an HTML template containing a `<div>` element with a class attribute of "btn-group action-btn" and two child elements, each representing a button with attributes for their IDs and associated actions. The function should extract the IDs and actions for these buttons and return them in a dictionary in the format `{button_id: action}`.
"""

import re

def extract_button_attributes(html_template: str) -> dict:
    button_attributes = {}
    pattern = r'(\w+-\w+)", "(\w+\.\w+)'

    matches = re.findall(pattern, html_template)
    for match in matches:
        button_id, action = match
        button_attributes[button_id] = action

    return button_attributes