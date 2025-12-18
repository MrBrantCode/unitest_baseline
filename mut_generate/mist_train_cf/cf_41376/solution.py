"""
QUESTION:
Extract the labels and corresponding input types from the given HTML code. 

Create a function `extractHTMLInfo(html)` that takes a string `html` representing the HTML code as input and returns a dictionary containing the labels as keys and the input types as values. The input HTML code is well-formed and has a structure where each label text is enclosed within a `<label>` tag and each input type is enclosed within an `<input>` tag. The function should be able to handle multiple occurrences of the label and input type pairs in the HTML code.
"""

import re

def extractHTMLInfo(html):
    pattern = r'<label for="(\w+)" class="control-label">(\w+)</label>\s+<input type="(\w+)"'
    matches = re.findall(pattern, html)
    info_dict = {}
    for match in matches:
        label_for, label_text, input_type = match
        info_dict[label_text] = input_type
    return info_dict