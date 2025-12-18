"""
QUESTION:
Convert a string representation of XML data to a dictionary object in Python. The function, `xml_to_dict`, should handle nested tags and attributes in the XML data. Nested elements should be nested within the parent dictionary as sub-dictionaries, and attributes should be included in the dictionary of the element with which they are associated.
"""

import xml.etree.ElementTree as ET

def xml_to_dict(element):
    #initialize an empty dictionary
    dict_data = {}
    
    #extract the element attributes and values
    for key, value in element.attrib.items():
        dict_data["@{}".format(key)] = value
    
    #process all nested elements
    for child in element:
        child_data = xml_to_dict(child)
        
        if child.tag in dict_data:
            if type(dict_data[child.tag]) is list:
                dict_data[child.tag].append(child_data)
            else:
                dict_data[child.tag] = [dict_data[child.tag], child_data]
        else:
            dict_data[child.tag] = child_data
    
    #extract text from element
    text = element.text
    if text:
        dict_data['#text'] = text

    return dict_data