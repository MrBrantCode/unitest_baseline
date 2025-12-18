"""
QUESTION:
Create a function `get_object_attributes(obj)` that takes an object `obj` as input and returns its top-level attribute names and values as a dictionary. The function should:

- Handle nested objects and lists within `obj`.
- Exclude any attributes within nested objects or lists.
- Validate attribute names to be strings consisting of alphanumeric characters and underscores.
- Validate attribute values to be of type `int`, `float`, `str`, or `bool`.
- Detect and raise an exception for circular references in nested objects.
- Exclude attributes with a value of `None` from the output.
- Sort the output alphabetically by attribute name.
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