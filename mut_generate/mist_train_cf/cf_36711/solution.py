"""
QUESTION:
Implement a function `extract_data_from_comment(comment: str) -> dict` that takes a string comment as input and returns a dictionary containing the extracted data from the comment. The comment contains data islands, which are sections of structured data embedded within the comments, represented as dictionaries in JSON-like format. If the comment does not contain any valid data islands, the function should return an empty dictionary.
"""

import re

def extract_data_from_comment(comment: str) -> dict:
    data_islands = re.findall(r'{(.*?)}', comment)
    extracted_data = {}
    for island in data_islands:
        try:
            data = eval('{' + island + '}')
            if isinstance(data, dict):
                extracted_data.update(data)
        except SyntaxError:
            pass
    return extracted_data