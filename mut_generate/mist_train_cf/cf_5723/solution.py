"""
QUESTION:
Create a function named `capitalize_strings` that takes a list of strings and returns a new list of strings. The function should capitalize the first alphabetic character of each string and make the rest of the alphabetic characters in the string lowercase, ignoring any non-alphabetic characters. The function should handle empty strings correctly and have a time complexity of O(n), where n is the total number of characters in all strings combined.
"""

def capitalize_strings(strings):
    capitalized_strings = []
    for string in strings:
        new_string = ""
        for i, char in enumerate(string):
            if char.isalpha():
                if i == 0 or (new_string and new_string[-1].isalpha() == False):
                    new_string += char.upper()
                else:
                    new_string += char.lower()
            else:
                new_string += char
        capitalized_strings.append(new_string)
    return capitalized_strings