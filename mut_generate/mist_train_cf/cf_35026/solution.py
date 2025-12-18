"""
QUESTION:
Write a function `parse_html_form(html_form: str) -> dict` that takes a string `html_form` representing a well-formed HTML form containing only input fields, and returns a dictionary where the keys are the input field names and the values are dictionaries containing the attributes of each input field. Each input field should have at least a `type` attribute and may have additional attributes. The function should assume that the input fields do not have nested forms and that they may have different types such as text, password, submit, etc.
"""

import re

def parse_html_form(html_form: str) -> dict:
    input_fields = re.findall(r'<input.*?>', html_form)
    parsed_fields = {}
    for field in input_fields:
        attributes = re.findall(r'(\w+)="([^"]*)"', field)
        field_dict = {attr[0]: attr[1] for attr in attributes}
        field_type = field_dict.get('type', '')
        if field_type:
            if 'name' in field_dict:
                field_name = field_dict['name']
            else:
                field_name = field_type.lower()
            parsed_fields[field_name] = field_dict
    return parsed_fields