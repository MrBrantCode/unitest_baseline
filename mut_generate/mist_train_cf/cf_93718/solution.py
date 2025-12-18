"""
QUESTION:
Convert a string from snake_case to camelCase using the function `snake_to_camel`. The input string is in snake_case format and contains only lowercase alphabets and underscores. It may have leading, trailing, or consecutive underscores. The function should remove leading and trailing underscores, treat multiple consecutive underscores as a single underscore, and capitalize the first letter of each word except the first word. The output string should be in camelCase format without any consecutive capital letters, except for the first letter of each word.
"""

def snake_to_camel(snake_case_string):
    words = snake_case_string.replace('__', '_').strip('_').split('_')
    camel_case_string = words[0].lower()
    for word in words[1:]:
        camel_case_string += word.capitalize()
    return camel_case_string