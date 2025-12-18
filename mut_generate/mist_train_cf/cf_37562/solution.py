"""
QUESTION:
Implement a function `iconToUnicode` that takes a string `iconName` as input and returns the Unicode representation of the icon. The function should use a predefined mapping of icon names to their Unicode representations and return "Icon not found" if the `iconName` is not in the mapping. Assume that the input `iconName` will always be a valid icon name in the mapping or not present in the mapping.
"""

def iconToUnicode(iconName):
    icon_map = {
        "arrow_back": "\u2190",
        "check_circle": "\u2713",
        # Add more icon mappings as needed
    }
    return icon_map.get(iconName, "Icon not found")