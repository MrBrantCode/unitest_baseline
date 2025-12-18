"""
QUESTION:
Create a function `countTags` that takes a string representing a PHP code snippet as input and returns a dictionary containing the counts of PHP tags and HTML elements present in the code snippet. The dictionary should have two keys: "phpTags" and "htmlElements". The value for each key should be another dictionary with the tag or element name as the key and the count as the value. PHP tags and HTML elements should be case-insensitive.
"""

import re

def countTags(code_snippet):
    php_tags = re.findall(r'<\?php|<\?|\?>', code_snippet, re.IGNORECASE)
    html_elements = re.findall(r'<\w+\b', code_snippet, re.IGNORECASE)
    
    php_tag_counts = {}
    html_element_counts = {}
    
    for tag in php_tags:
        tag = tag.lower()
        php_tag_counts[tag] = php_tag_counts.get(tag, 0) + 1
    
    for element in html_elements:
        element = element[1:].lower()  # Remove '<' and convert to lowercase
        html_element_counts[element] = html_element_counts.get(element, 0) + 1
    
    return {
        "phpTags": php_tag_counts,
        "htmlElements": html_element_counts
    }