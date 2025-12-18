"""
QUESTION:
Implement the `static_or_class_method` function, which takes a string as input and returns whether the given method should be implemented as a static method or a class method in a Python class. The method can either modify class-level attributes or not modify any attributes at all, but it does not need to access instance-specific data.
"""

def static_or_class_method(modify_class_attributes):
    """
    Returns whether the given method should be implemented as a static method or a class method in a Python class.
    
    Parameters:
    modify_class_attributes (bool): Whether the method can modify class-level attributes or not.
    
    Returns:
    str: "static method" if the method should be implemented as a static method, "class method" otherwise.
    """
    if modify_class_attributes:
        return "class method"
    else:
        return "static method"