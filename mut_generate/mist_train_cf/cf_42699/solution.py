"""
QUESTION:
Extract the titles and contents of sections from a given text in a specific format. The section format starts with a leading period followed by a double colon, containing a title and content enclosed within double colons and the content following immediately after the title. 

Create a function `extract_sections(text: str) -> dict` that takes a string `text` as input and returns a dictionary where the keys are the titles of the sections and the values are the corresponding contents.
"""

import re

def extract_sections(text: str) -> dict:
    sections = re.findall(r'\.\.\s*wikisection::\s*(.*?)\s*:title:\s*(.*?)\s*:content:\s*(.*?)\n', text, re.DOTALL)
    section_dict = {title.strip(): content.strip() for _, title, content in sections}
    return section_dict