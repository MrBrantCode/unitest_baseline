"""
QUESTION:
Write a function `parseValidationMessages` that takes a string containing a code snippet from a Laravel application's language file as input, where each line follows the format "<validation_rule>.<error_type>" => __('<error_message>'). The function should parse the code snippet, extract the validation rules and their corresponding error messages, and return a dictionary containing the validation rules as keys and their corresponding error messages as values.
"""

import re

def parseValidationMessages(code_snippet: str) -> dict:
    validation_messages = {}
    pattern = r'"(.*?)".*?=>.*?__\(\'(.*?)\'\)'
    matches = re.findall(pattern, code_snippet)
    for match in matches:
        validation_messages[match[0]] = match[1]
    return validation_messages