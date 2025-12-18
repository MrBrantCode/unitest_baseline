"""
QUESTION:
Write a function `parse_svg_snippet(svg_snippet: str) -> dict` that takes an SVG code snippet as input and extracts the type of transformation, its parameters, and the id of the group element. The input SVG snippet should be in the format `transform="type(param1, param2,...)" > <g id="groupId">` where "type" is the transformation type, "param1, param2,..." are the transformation parameters, and "groupId" is the group id. The function should return a dictionary with keys "transformation_type", "transformation_parameters", and "group_id" containing the extracted information. If the input does not match the expected format, the function should return an empty dictionary.
"""

import re

def parse_svg_snippet(svg_snippet: str) -> dict:
    pattern = r'transform="(\w+)\(([\d.,\s]+)\)"\s*>\s*<g id="(\w+)">'
    match = re.search(pattern, svg_snippet)
    if match:
        transformation_type = match.group(1)
        transformation_parameters = match.group(2).split(', ')
        group_id = match.group(3)
        return {
            "transformation_type": transformation_type,
            "transformation_parameters": transformation_parameters,
            "group_id": group_id
        }
    else:
        return {}