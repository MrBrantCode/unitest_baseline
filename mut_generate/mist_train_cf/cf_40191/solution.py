"""
QUESTION:
Write a function called `parse_input_elements` that takes a string `html_code` representing the HTML code of a form and returns a list of dictionaries, where each dictionary represents an input element and contains its attributes. The input element is defined as any HTML tag that starts with `<input` and ends with `>`, and the attributes are defined as any key-value pairs within the tag.
"""

import re

def parse_input_elements(html_code):
    input_elements = re.findall(r'<input(.*?)>', html_code)
    parsed_elements = []
    for element in input_elements:
        attributes = re.findall(r'(\S+)=["\'](.*?)["\']', element)
        element_dict = {}
        for attr in attributes:
            element_dict[attr[0]] = attr[1]
        parsed_elements.append(element_dict)
    return parsed_elements