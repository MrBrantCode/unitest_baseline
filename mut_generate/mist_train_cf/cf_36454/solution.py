"""
QUESTION:
Implement the function `parse_html_form(html)` that takes an HTML string `html` representing a form enclosed within `<form>` and `</form>` tags. Each input field is represented by an `<input>` tag with a `name` attribute and a `value` attribute. The function should return a dictionary containing the input fields' names as keys and their corresponding values. The input HTML string format is guaranteed to match the specified pattern.
"""

import re

def parse_html_form(html):
    form_data = {}
    input_fields = re.findall(r'<input name="([^"]+)" value="([^"]+)"', html)
    for field in input_fields:
        form_data[field[0]] = field[1]
    return form_data