"""
QUESTION:
Create a function called `to_camel_case` that takes a string as input and returns the string in CamelCase format. The string should be converted to CamelCase only if it contains at least one uppercase letter and at least one digit. If the string does not meet these conditions, return the original string. The input string may contain underscores and letters, both uppercase and lowercase, and digits.
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