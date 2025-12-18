"""
QUESTION:
Create a function named `translator` that takes a string as input, converts all lowercase letters to uppercase, and replaces specified symbols and numeric characters with their word equivalents in a non-native language. The function should handle special characters, escape sequences, and numeric characters, and not throw any errors when encountering characters not in the predefined mapping.
"""

def translator(string):
    symbol_dict = {
        '&': 'et',
        '@': 'arobase',
        '1': 'un',
        '\n': 'newline'
    }
    translated_string = ""
    
    for char in string:
        if char.islower():
            translated_string += char.upper()
        elif char in symbol_dict.keys():
            translated_string += symbol_dict[char]
        else:
            translated_string += char
            
    return translated_string