"""
QUESTION:
Write a function `extract_license_text` that takes a string `input_str` as input. The function should return the text between the first and second occurrence of the word "License" (case-insensitive), inclusive, in the input string. If the word "License" appears less than twice, return an empty string.
"""

def extract_license_text(input_str):
    start_index = input_str.lower().find('license')
    if start_index != -1:
        end_index = input_str.lower().find('license', start_index + 1)
        if end_index != -1:
            return input_str[start_index:end_index + len('License')]
    return ''