"""
QUESTION:
Design a function named `symbol_translator` that takes a string `text`, a dictionary `symbol_dict` containing translations of symbols for different languages, and a string `language` indicating the desired language for symbol translations. The function should convert all lowercase letters in the input string to uppercase and replace any symbols with their corresponding names in the specified language. The function should also handle special characters, converting them into their word equivalents. The function should return the modified string. The `symbol_dict` dictionary is expected to have symbols as keys and dictionaries with language codes as keys and translations as values.
"""

def symbol_translator(text, symbol_dict, language):
    output = ""
    for char in text:
        if char.isalpha():
            output += char.upper()
        elif char in symbol_dict:
            output += symbol_dict[char][language]
        else:
            output += char if char != '\\' else 'backslash'
    return output