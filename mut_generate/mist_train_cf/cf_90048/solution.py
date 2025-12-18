"""
QUESTION:
Implement a function `get_object_attributes` that takes an object as input and returns a dictionary containing its top-level attribute names and values. The function should:

- Handle nested objects and lists within the input object.
- Only return the names and values of the top-level attributes, excluding any attributes within nested objects or lists.
- Validate that attribute names consist of alphanumeric characters and underscores.
- Validate that attribute values are of type int, float, str, or bool.
- Exclude attributes with a value of None from the output.
- Sort the output alphabetically by attribute name.
- Raise an exception if the input object contains any invalid attribute names, attribute types, or circular references.
"""

def get_object_attributes(obj):
    def check_attribute_name(attribute_name):
        if not isinstance(attribute_name, str) or not attribute_name.isidentifier():
            raise Exception(f"Invalid attribute name: {attribute_name}")
    
    def get_attributes(obj, parent=None, visited=set()):
        if obj is None:
            return {}
        
        if id(obj) in visited:
            raise Exception("Circular reference detected")
        visited.add(id(obj))
        
        if isinstance(obj, (int, float, str, bool)):
            return {parent: obj} if parent is not None else {}
        
        if isinstance(obj, (list, tuple)):
            attributes = {}
            for i, value in enumerate(obj):
                name = f"{parent}[{i}]"
                attributes.update(get_attributes(value, parent=name, visited=visited))
            return attributes
        
        if isinstance(obj, dict):
            attributes = {}
            for key, value in obj.items():
                check_attribute_name(key)
                name = f"{parent}.{key}" if parent is not None else key
                attributes.update(get_attributes(value, parent=name, visited=visited))
            return attributes
        
        raise Exception(f"Invalid attribute type: {type(obj)}")
    
    attributes = get_attributes(obj)
    return {k: v for k, v in sorted(attributes.items()) if v is not None}