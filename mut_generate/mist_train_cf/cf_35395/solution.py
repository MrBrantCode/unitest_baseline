"""
QUESTION:
Create a function called `extractHTMLContent` that takes two parameters: `tag_name` and `input_string`. The function should extract the content within the specified HTML `tag_name` from the given `input_string` and return it as a string. The function should return "Tag not found or empty content" if the specified tag is not found or the content is empty.
"""

import re

def extractHTMLContent(tag_name, input_string):
    pattern = r"<" + tag_name + r".*?>(.*?)</" + tag_name + r">"
    match = re.search(pattern, input_string, re.DOTALL)
    if match:
        return match.group(1)
    else:
        return "Tag not found or empty content"