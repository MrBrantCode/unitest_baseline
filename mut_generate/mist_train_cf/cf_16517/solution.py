"""
QUESTION:
Write a function `convert_to_json(element, config)` that converts an XML element to a JSON object following the naming conventions specified in the `config` dictionary. The function should handle XML elements with attributes and any level of nesting. The `element` is an XML element parsed into a dictionary, and the `config` is a dictionary containing the naming conventions. The function should return a JSON object.
"""

def convert_to_json(element, config):
    json_dict = {}
    
    # Convert attributes to JSON
    if '@id' in element:
        json_dict['id'] = element['@id']
    
    # Convert elements to JSON
    for key, value in element.items():
        if key != '@id':
            if isinstance(value, dict):
                json_dict[config.get(key, key)] = convert_to_json(value, config)
            else:
                json_dict[config.get(key, key)] = value
    
    return json_dict