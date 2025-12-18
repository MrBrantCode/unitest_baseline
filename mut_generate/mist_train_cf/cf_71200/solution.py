"""
QUESTION:
Write a function named `highestPowerExtension` that takes a class name (string) and a list of extensions as input. Each extension is a list containing a string (the extension name) and another string (the method name). The function should return a string in the format `ClassName.HighestPowerExtension.MethodName`. The highest power extension is the one with the highest sum of ASCII values of its characters, and in case of a tie, the one that appears first in the list. The method name should also be the first one implemented by the highest power extension.
"""

def highestPowerExtension(class_name, extensions):
    """
    Returns a string representing the highest power extension.

    Args:
        class_name (str): The class name.
        extensions (list): A list of extensions, where each extension is a list containing 
            a string (the extension name) and another string (the method name).

    Returns:
        str: A string in the format `ClassName.HighestPowerExtension.MethodName`.
    """
    highest = ['', 0, '']
    for extension in extensions:
        power = sum(ord(char) for char in extension[0])
        if power > highest[1]:
            highest = [extension[0], power, extension[1]]
    return f"{class_name}.{highest[0]}.{highest[2]}"