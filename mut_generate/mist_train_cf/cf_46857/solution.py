"""
QUESTION:
Create a function `replace_characters` that takes a string `string` and a dictionary `mapping` as input. The function should replace all non-alphabetic characters in the string with their corresponding values in the `mapping` dictionary. If a non-alphabetic character is not found in the dictionary, it should be replaced with the '&' symbol. After replacement, the function should remove any consecutive duplicates of the substituted symbols.
"""

def replace_characters(string, mapping):
    default = "&"
    new_string = ""
    for char in string:
        if not char.isalpha():
            new_string += mapping.get(char, default)
        else:
            new_string += char
    # removing consecutive duplicates
    i = 0
    while i < len(new_string) - 1:
        if new_string[i] == new_string[i+1] and new_string[i] in mapping.values():
            new_string = new_string[:i] + new_string[i+1:]
        else:
            i += 1
    return new_string