"""
QUESTION:
Implement the `process_data` function to extract the description attribute from the `attrs` dictionary based on the given `name`. The function should take in three parameters: `udata` (an object of class `UData`), `name` (a string), and `attrs` (a dictionary). It should return the description attribute if found; otherwise, it should return an empty string. 

The `get_attr` function is available to extract a specific attribute from the `attrs` dictionary based on the given `name` and attribute name.
"""

def process_data(udata, name, attrs):
    return get_attr(attrs, 'desc', name)

def get_attr(attrs, attr_name, name):
    if name in attrs:
        return attrs[name]
    else:
        return ""