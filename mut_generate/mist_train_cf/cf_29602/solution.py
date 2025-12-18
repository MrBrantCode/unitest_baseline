"""
QUESTION:
Write a function `extractSectionContent(html)` that takes a string `html` as input, representing a snippet of HTML code. The function should return the content of the section, defined as the text between the opening `<section>` tag and the closing `</section>` tag, excluding any leading or trailing whitespace. Assume that the input HTML is well-formed and that the section tags will not be nested within each other.
"""

import re

def extractSectionContent(html):
    section_content = re.search(r'<section>(.*?)</section>', html, re.DOTALL)
    if section_content:
        return section_content.group(1).strip()
    else:
        return ""