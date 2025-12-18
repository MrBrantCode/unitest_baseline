"""
QUESTION:
Create a function called `to_camel_case` that takes a string as input and returns the string in CamelCase if it contains at least one uppercase letter and at least one digit. Otherwise, the function should return the original string. The input string is separated by underscores.
"""

def to_camel_case(string):
    if any(char.isupper() for char in string) and any(char.isdigit() for char in string):
        words = string.split('_')
        camel_case_words = [words[0]]
        for word in words[1:]:
            camel_case_words.append(word.capitalize())
        return ''.join(camel_case_words)
    else:
        return string