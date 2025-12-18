"""
QUESTION:
Write a Python function `generate_output` that takes in a dictionary `language_info` and a string `banner` as parameters. The dictionary `language_info` contains keys 'name' and 'mimetype', and the string `banner` represents a banner message. The function should return a formatted output string based on the 'mimetype' in `language_info`. If the 'mimetype' is 'text/plain', the output string should be "<banner> - <name> language (plain text)". If the 'mimetype' is 'text/html', the output string should be "<banner> - <name> language (HTML)". For other 'mimetype' values, the output string should be "<banner> - <name> language". Assume the input dictionary and string are always valid.
"""

def generate_output(language_info, banner):
    if language_info['mimetype'] == 'text/plain':
        return f"{banner} - {language_info['name']} language (plain text)"
    elif language_info['mimetype'] == 'text/html':
        return f"{banner} - {language_info['name']} language (HTML)"
    else:
        return f"{banner} - {language_info['name']} language"