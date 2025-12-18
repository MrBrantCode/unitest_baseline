"""
QUESTION:
Create a function `capitalize_strings` that takes a list of strings as input and returns a new list where the first letter of each string is capitalized and the rest of the letters are in lowercase. Implement this without using built-in string manipulation functions like `capitalize()` or `title()`, and ensure a time complexity of O(n), where n is the total number of characters in all strings combined.
"""

def capitalize_strings(strings):
    capitalized_strings = []
    for string in strings:
        capitalized_string = ""
        for i, char in enumerate(string):
            if i == 0:
                capitalized_string += char.upper()
            else:
                capitalized_string += char.lower()
        capitalized_strings.append(capitalized_string)
    return capitalized_strings