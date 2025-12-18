"""
QUESTION:
Write a function `extract_meta_tags` that takes a string `html_code` as input and returns a dictionary containing the extracted meta tag attributes and their values. The function should parse the HTML code to identify and extract the attributes and their corresponding values from the meta tags, handling cases where multiple values exist for the same attribute by storing them in a list.
"""

import re

def extract_meta_tags(html_code):
    meta_tags = re.findall(r'<meta\s+([^>]+)>', html_code)
    meta_info = {}
    for tag in meta_tags:
        attributes = re.findall(r'(\w+)\s*=\s*\"([^\"]+)\"', tag)
        for attr, value in attributes:
            if attr in meta_info:
                if isinstance(meta_info[attr], list):
                    meta_info[attr].append(value)
                else:
                    meta_info[attr] = [meta_info[attr], value]
            else:
                meta_info[attr] = value
    return meta_info