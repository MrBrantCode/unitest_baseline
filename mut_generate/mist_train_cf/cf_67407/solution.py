"""
QUESTION:
Create a function `Strongest_Extension` that takes a class label (string) and a collection of extension labels (list of strings) as input. The function should calculate the "vigor" of each extension by subtracting the count of lowercase letters from the count of uppercase letters. It should then return a string combining the class label and the extension with the highest vigor, separated by a period. If multiple extensions have the same highest vigor, the function should prioritize the one appearing first in the list.
"""

def Strongest_Extension(class_name, extensions):
    """
    This function calculates the 'vigor' of each extension in a list by subtracting 
    the count of lowercase letters from the count of uppercase letters and returns 
    a string combining the class label and the extension with the highest vigor.

    Args:
        class_name (str): The class label.
        extensions (list): A list of extension labels.

    Returns:
        str: A string combining the class label and the extension with the highest vigor.
    """
    def calculate_vigor(extension):
        """Calculate the vigor of an extension."""
        return sum(1 for c in extension if c.isupper()) - sum(1 for c in extension if c.islower())

    return class_name + "." + max(extensions, key=calculate_vigor)