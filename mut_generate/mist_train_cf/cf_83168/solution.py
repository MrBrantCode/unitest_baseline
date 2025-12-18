"""
QUESTION:
Write a function `json_to_xml` that converts a given JSON object to an XML string. The function should support nested JSON structures with varying depth levels and include a specified attribute in the XML output. The function should take two parameters: the JSON object and the attribute to be used in the XML output.
"""

import json

def json_to_xml(obj, tag):
    xml = ''
    if isinstance(obj, dict):
        for k, v in obj.items():
            xml += f'<{k}>{json_to_xml(v, tag)}</{k}>'
    elif isinstance(obj, list):
        for item in obj:
            xml += f'<{tag}>{json_to_xml(item, tag)}</{tag}>'
    else:
        xml = str(obj)
    return xml