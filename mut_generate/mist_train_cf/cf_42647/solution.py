"""
QUESTION:
Write a function `parse_css` that takes a CSS snippet as input and returns a list of tuples, where each tuple contains a selector and its corresponding properties as a dictionary. The function should parse the CSS snippet and extract the selectors and their properties, ignoring any nested structures and only considering the top-level selectors. The function should return a list of tuples, where each tuple contains a selector as a string and its properties as a dictionary. The dictionary should have the property names as keys and the property values as values.
"""

import re

def parse_css(css_snippet):
    selectors = re.findall(r'([a-zA-Z0-9\s.#]+)\s*{([^}]*)}', css_snippet)
    result = []
    for selector, properties in selectors:
        properties_dict = {}
        properties_list = properties.split(';')
        for prop in properties_list:
            prop = prop.strip()
            if prop:
                key, value = prop.split(':')
                properties_dict[key.strip()] = value.strip()
        result.append((selector.strip(), properties_dict))
    return result