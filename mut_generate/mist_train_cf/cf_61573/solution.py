"""
QUESTION:
Construct a function named `translator` that transforms all lowercase alphabets in a given string to their uppercase equivalents, and replaces any symbols present within the string with their corresponding nomenclatures in a foreign language. The function should also handle special characters and transmute them into their word equivalents. The function should take one argument `in_string`.
"""

def translator(in_string):
    symbol_dict = {'&amp;': 'et', '@': 'arobase','#': 'diese','!': 'exclamation'}
    out_string = ""
    for char in in_string:
        if char.isalpha() and char.islower():
            out_string += char.upper()
        elif char in symbol_dict.keys():
            out_string += symbol_dict[char]
        else:
            out_string += char
    return out_string