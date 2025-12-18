"""
QUESTION:
Write a function `unnecessary_class` that verifies whether a given class name follows the naming convention rules or not. The rules are:
- The class name should not contain 'XC', 'UI', or 'Model' (case insensitive).
- The class name should not end with 'model' (case insensitive).
If the class name does not follow these rules, the function should return a message indicating that the class may not need to exist. The function should work with SwiftLint's regex which is not multiline.
"""

def unnecessary_class(class_name):
    """
    Verifies whether a given class name follows the naming convention rules or not.
    
    Args:
    class_name (str): The name of the class to be verified.
    
    Returns:
    str: A message indicating whether the class may not need to exist or not.
    """
    if 'XC' in class_name.upper() or 'UI' in class_name.upper() or 'Model' in class_name.upper() or class_name.upper().endswith('MODEL'):
        return "This class may not need to exist."
    else:
        return ""