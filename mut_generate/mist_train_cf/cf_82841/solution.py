"""
QUESTION:
Construct the `Potent_Extension` function, which takes a class name (as a string) and an array of extension identifiers. The function should return a string by appending the most potent extension identifier to the class name. The potency of an extension identifier is calculated by subtracting the number of lowercase characters from the number of uppercase characters. If multiple identifiers have the same potency, the function should return the first one in the array.
"""

def Potent_Extension(class_name, extensions):
    """
    Appends the most potent extension identifier to the class name.
    
    The potency of an extension identifier is calculated by subtracting the number of lowercase characters 
    from the number of uppercase characters. If multiple identifiers have the same potency, the function 
    returns the first one in the array.

    Args:
    class_name (str): The class name as a string.
    extensions (list): A list of extension identifiers.

    Returns:
    str: The class name with the most potent extension identifier appended.
    """

    max_potency = float('-inf')  # Initialize max potency as negative infinity
    most_potent_extension = ""  # Most potent extension string

    for extension in extensions:
        potency = sum(1 if char.isupper() else -1 if char.islower() else 0 for char in extension)
        if potency > max_potency:
            max_potency = potency
            most_potent_extension = extension

    return class_name + "." + most_potent_extension