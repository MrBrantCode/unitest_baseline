"""
QUESTION:
Create a function `processHTML` that takes a string `htmlSnippet` as input. The function should return a dictionary containing the text content within the `<p>` tags, indexed by their order of appearance in the HTML snippet, and a boolean value indicating whether the PHP code snippet is present in the input.
"""

import re

def processHTML(htmlSnippet):
    textContent = re.findall(r'<p>(.*?)</p>', htmlSnippet)
    hasPHPCode = '<?php' in htmlSnippet
    return {"textContent": textContent, "hasPHPCode": hasPHPCode}