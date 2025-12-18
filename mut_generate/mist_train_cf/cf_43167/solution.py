"""
QUESTION:
Implement a function `dict_to_xml` that takes a dictionary as input and returns a well-formed XML string. The input dictionary has three keys: 'question', 'content', and 'context'. The output XML string should have the format `<chat><question>value</question><content>value</content><context>value</context></chat>`. Ensure the XML string is properly formatted with indentation and newlines.
"""

def dict_to_xml(data):
    xml_string = "<chat>\n"
    for key, value in data.items():
        xml_string += f"    <{key}>{value}</{key}>\n"
    xml_string += "</chat>"
    return xml_string