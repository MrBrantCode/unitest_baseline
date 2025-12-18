"""
QUESTION:
Write a function `get_namespace_of_attribute` that determines whether an attribute belongs to a namespace in an XML document. Assume the XML document uses a default namespace and some attributes may have an explicitly defined namespace prefix.
"""

def get_namespace_of_attribute(element, attribute_name, attribute_value):
    """
    Determine whether an attribute belongs to a namespace in an XML document.
    
    Args:
        element (xml.etree.ElementTree.Element): The XML element that the attribute belongs to.
        attribute_name (str): The name of the attribute.
        attribute_value (str): The value of the attribute.
        
    Returns:
        str: The namespace of the attribute if it has one, 'local' if it's a local attribute, and None if it's not found.
    """
    # If the attribute has an explicitly defined namespace prefix, return the namespace
    if '}' in attribute_name:
        namespace, _ = attribute_name.split('}')
        return namespace[1:]  # Remove the '{' character
    
    # Check if the attribute is one of the special attributes that are in a namespace by definition
    if attribute_name in ['xml:lang', 'xml:space', 'xml:base']:
        return 'http://www.w3.org/XML/1998/namespace'
    
    # If the attribute does not have a prefix, it's a local attribute
    return 'local'