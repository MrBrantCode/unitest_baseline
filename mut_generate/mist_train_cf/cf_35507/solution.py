"""
QUESTION:
Implement a function `parseForm(html: str) -> dict` that takes a string `html` representing an HTML form code and returns a dictionary containing the form's action URL and a dictionary of input field names and their corresponding values. Assume that the HTML form code will always have a valid structure with the action attribute defined and input fields containing names and values.
"""

import re

def parseForm(html: str) -> dict:
    form_data = {"action": "", "inputs": {}}

    action_match = re.search(r'<form.*?action="(.*?)"', html)
    if action_match:
        form_data["action"] = action_match.group(1)

    input_matches = re.findall(r'<input.*?name="(.*?)".*?value="(.*?)"', html)
    for name, value in input_matches:
        form_data["inputs"][name] = value

    return form_data