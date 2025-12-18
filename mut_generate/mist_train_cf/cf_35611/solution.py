"""
QUESTION:
Create a function named `extract_form_ids` that takes an HTML snippet as input and returns a list of form IDs present in the snippet. The function should be able to extract the IDs from the 'id' attribute of the 'form' tags in the HTML snippet.
"""

import re

def extract_form_ids(html_snippet):
    form_ids = re.findall(r'<form.*?id="(.*?)"', html_snippet)
    return form_ids