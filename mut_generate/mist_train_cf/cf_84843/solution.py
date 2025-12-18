"""
QUESTION:
Create a function named `extract_html_props` that takes a string of HTML code as input and returns a list of tuples, where each tuple contains a property name and its corresponding value from the HTML tags. The function should be able to handle both regular and self-closing HTML tags. The properties should be extracted in the format of ("property_name", "property_value").
"""

import re

def extract_html_props(html_string):
    # Regex to match html tags
    tag_pattern = re.compile(r'<[^>]+>')
    
    # List to store the properties
    prop_list = []

    for tag in tag_pattern.findall(html_string):

        # For self-closing tags (e.g. <img/> <br/>)
        if tag.endswith('/>'):
            tag = tag[:-2]

        # Regex for matching properties within an HTML tag
        prop_pattern = re.compile(r'(\S+)=["\']?((?:.(?!["\']?\s+(?:\S+)=|[>"\']))+.)["\']?')

        for prop in prop_pattern.findall(tag):
            prop_list.append(prop)

    return prop_list