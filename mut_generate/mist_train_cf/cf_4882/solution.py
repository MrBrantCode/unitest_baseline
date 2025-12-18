"""
QUESTION:
Create a function `generate_object(strings)` that takes an array of strings and returns a dictionary with the strings as keys and their lengths as values. The function should only include strings with a length of at least 5 characters, containing no special characters or numbers, and having no repeating characters. The dictionary should be sorted in descending order by string length.
"""

def generate_object(strings):
    obj = {}
    for string in strings:
        if len(string) >= 5 and not any(char.isdigit() or not char.isalpha() for char in string):
            if len(set(string)) == len(string):
                obj[string] = len(string)
    return {k: v for k, v in sorted(obj.items(), key=lambda item: item[1], reverse=True)}