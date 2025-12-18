"""
QUESTION:
Write a function named `snake_to_camel` that takes a string in snake_case as input and returns its camelCase equivalent. The input string will only contain lowercase alphabets and underscores, will not be empty, and will not start with an underscore. The input string may contain multiple consecutive underscores, leading or trailing underscores, or underscores before and after a word, which should be treated as a single underscore in the final output. The output string should not have any consecutive capital letters, except for the first letter of each word.
"""

def snake_to_camel(snake_case_string):
    words = snake_case_string.split('_')
    camel_case_string = words[0].lower()
    for word in words[1:]:
        camel_case_string += word.capitalize()
    return camel_case_string