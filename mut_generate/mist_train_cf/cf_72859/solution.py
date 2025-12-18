"""
QUESTION:
Design a function `convert_to_camel_case(s)` that converts an input string `s` into its corresponding camel case format. The function should take a string as input and return the camel case version of the string. The input string contains multiple words separated by spaces, and the output should be a single string with the first word in lowercase and the first letter of each subsequent word capitalized.
"""

def convert_to_camel_case(s):
    words = s.split(' ')
    capitalized_words = [words[0].lower()] + [word.capitalize() for word in words[1:]]
    camel_case_string = ''.join(capitalized_words)
    return camel_case_string