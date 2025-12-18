"""
QUESTION:
Create a function called `generate_property_code` that takes in two parameters, `property_type` and `property_name`. The function should return a tuple containing the lines of code for adding a property in the .h interface, the property declaration in the .h file, the synthesize statement in the .m file, and the release statement in the .m dealloc method. Do not include any actual implementation of the property or dealloc method, just the individual lines of code.
"""

def generate_property_code(property_type, property_name):
    """
    Generates the code for adding a property in the .h interface, 
    the property declaration in the .h file, the synthesize statement 
    in the .m file, and the release statement in the .m dealloc method.

    Args:
        property_type (str): The type of the property.
        property_name (str): The name of the property.

    Returns:
        tuple: A tuple containing the lines of code.
    """
    h_interface = f"@property (nonatomic, retain) {property_type} *{property_name};"
    h_declaration = f"{property_type} *{property_name};"
    m_synthesize = f"@synthesize {property_name};"
    m_release = f"[{property_name} release];"

    return h_interface, h_declaration, m_synthesize, m_release