"""
QUESTION:
Write a function named `advanced_string_formatting` that takes three parameters: an original string (`orig_str`), a delimiter string, and a dictionary (`format_options`) containing formatting options. The `format_options` dictionary may contain the following keys: `"reverse"`, `"uppercase"`, and `"capitalize_words"`. Based on the values of these keys, the function should reverse the string, convert it to uppercase, and capitalize each word, respectively. The function should then return the formatted string with the delimiter prepended and appended to it.
"""

def advanced_string_formatting(orig_str, delimiter, format_options):
    # Reverse the string if the "reverse" format option is True
    if format_options.get("reverse", False):
        orig_str = orig_str[::-1]

    # Convert the string to uppercase if the "uppercase" format option is True
    if format_options.get("uppercase", False):
        orig_str = orig_str.upper()

    # Capitalize each word in the string if the "capitalize_words" format option is True
    if format_options.get("capitalize_words", False):
        orig_str = " ".join([word.capitalize() for word in orig_str.split(" ")])

    # Add the delimiter to the beginning and end of the string
    formatted_str = delimiter + orig_str + delimiter

    return formatted_str