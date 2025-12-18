"""
QUESTION:
Create a function called `extract_template_name` that takes a string `file_content` as input and returns the template name extracted from the string. The template name is denoted by the format `Template Name: <name>` within a PHP comment block (`/** */`). If the template name is not found or the input string is empty, the function should return "Template name not found".
"""

import re

def extract_template_name(file_content):
    match = re.search(r'/\*\*\s*Template Name:\s*(.*?)\s*\*/', file_content)
    if match:
        return match.group(1)
    else:
        return "Template name not found"