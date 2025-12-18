"""
QUESTION:
Write a function that takes a class name as input and returns whether calling the class name followed by parentheses is invoking the class constructor or a function. Assume the class is one of the built-in data types in Python.
"""

def is_class_constructor(class_name):
    """
    This function checks whether calling a class name followed by parentheses is 
    invoking the class constructor or a function.

    Args:
        class_name (str): The name of the class to check.

    Returns:
        str: A message indicating whether it's a class constructor or a function.
    """
    # Check if the class name is one of the built-in data types in Python
    if class_name in ['str', 'int', 'complex', 'bool', 'float', 'list', 'tuple', 'dict', 'set']:
        return f"Calling {class_name}() is invoking the class constructor."
    else:
        return f"Calling {class_name}() is invoking a function."