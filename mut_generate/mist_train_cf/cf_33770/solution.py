"""
QUESTION:
Create a function `extractLabels` that takes a string of HTML code as input and returns a dictionary. The dictionary's keys are the text of the `label` tags and the values are the attributes of the `label` tags as a string. The HTML code is well-formed, and each label tag has attributes in the form of key-value pairs within the opening tag.
"""

import re

def extractLabels(html_code):
    label_pattern = r'<label\s+([^>]+)>([^<]+)</label>'
    labels = re.findall(label_pattern, html_code)
    label_attributes = {}
    for attributes, label in labels:
        attribute_str = ' '.join(attributes.split())
        label_attributes[label.strip()] = attribute_str
    return label_attributes