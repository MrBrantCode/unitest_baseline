"""
QUESTION:
Create a function named `decompose_css` that takes a string containing conjoined HTML and CSS as input. The function should return a dictionary where the keys are the HTML tags (e.g., 'body', 'h1') and the values are dictionaries of their corresponding CSS attributes. The function should assume that there are no nested CSS definitions and that each closing curly brace '}' signifies the end of an attribute set.
"""

import re

def decompose_css(html_css_string):
    """
    Decompose a string containing conjoined HTML and CSS into a dictionary where 
    the keys are the HTML tags and the values are dictionaries of their corresponding CSS attributes.

    Args:
    html_css_string (str): A string containing conjoined HTML and CSS.

    Returns:
    dict: A dictionary where the keys are the HTML tags and the values are dictionaries of their corresponding CSS attributes.
    """

    css_fragment = re.findall(r'<style>.*?</style>', html_css_string)
    if not css_fragment:
        return {}

    css_attributes = re.findall(r'{.*?}', css_fragment[0])
    css_dict = {}

    for attribute_set in css_attributes:
        attribute_set = attribute_set.replace("{", "").replace("}", "")
        attributes = attribute_set.split(";")
        for attribute in attributes:
            if ":" in attribute:
                key, value = attribute.split(":")
                id_name = re.findall(r'\b(\w+)\b\s*{', css_fragment[0].split('}')[0])
                if id_name:
                    id_name = id_name[0]
                    if id_name in css_dict:
                        css_dict[id_name].update({key.strip(): value.strip()})
                    else:
                        css_dict[id_name] = {key.strip(): value.strip()}
                    css_fragment[0] = css_fragment[0].replace('}', '', 1)
    return css_dict