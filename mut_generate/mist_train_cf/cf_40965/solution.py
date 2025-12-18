"""
QUESTION:
Create a function `parseHTML` that takes a string of HTML as input, removes all HTML tags, and returns the extracted text content as a single string with no leading or trailing whitespace. The function should handle basic HTML tags such as `<h1>`, `<p>`, and `<div>`, and ignore any other HTML elements or attributes.
"""

import re

def parseHTML(html):
    clean_text = re.sub('<[^<]+?>', '', html)
    return clean_text.strip()