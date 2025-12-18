"""
QUESTION:
Create a custom markup extension in XAML that instantiates a class with specified properties and returns an object. The custom markup extension should be usable in XAML like `{MyCustomObject Field1=Foo, Field2=Bar}`. Additionally, determine if it's possible to programmatically parse a XAML string and return the corresponding object, resolving any bindings or custom markup extensions.
"""

import xml.etree.ElementTree as ET

def my_custom_object(field1, field2):
    # Create a new XML element for the custom object
    obj = ET.Element('MyCustomObject')
    obj.set('Field1', field1)
    obj.set('Field2', field2)
    
    # Return the custom object as an ElementTree object
    return ET.ElementTree(obj)