"""
QUESTION:
Write a function called `json_to_xml` that converts a given JSON object into an equivalently structured XML result. The function should be able to handle any level of nesting and variety of data types in the JSON structure's values. It should preserve the depth, ordering, and values of the original JSON structure. The function should also include proper error handling for invalid JSON inputs.
"""

import json
from xml.dom.minidom import Document

def json_to_xml(json_obj, line_padding=""):
    dom = Document()

    json_obj_type = type(json_obj)

    if json_obj_type is list:
        for sub_elem in json_obj:
            dom.appendChild(json_to_xml(sub_elem, line_padding))

        return dom

    if json_obj_type is dict:
        xml = dom.createElement('root')
        dom.appendChild(xml)
        for tag_name in json_obj:
            if isinstance(json_obj[tag_name], dict):
                child_node = json_to_xml(json_obj[tag_name], line_padding)
                child_node.tagName = tag_name
                xml.appendChild(child_node)
            elif isinstance(json_obj[tag_name], list):
                for i, item in enumerate(json_obj[tag_name]):
                    child_node = dom.createElement(tag_name)
                    child_node.appendChild(dom.createTextNode(str(item)))
                    xml.appendChild(child_node)
            else:
                child_node = dom.createElement(tag_name)
                child_node.appendChild(dom.createTextNode(str(json_obj[tag_name])))
                xml.appendChild(child_node)
        return xml

    return dom.createTextNode(str(json_obj))