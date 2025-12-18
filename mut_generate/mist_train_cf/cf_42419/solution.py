"""
QUESTION:
Create a function called `extract_html_tags` that takes a string `text` as input and returns a list of unique HTML tags found in the text, sorted in lexicographical order. The function should only consider the tag name and not any attributes, and the tags should be in their opening form (e.g., `<p>`, not `</p>`).
"""

import re

def extract_html_tags(text):
    tags = re.findall(r'<(\w+)[^>]*>', text)  # Use regular expression to find all HTML tags
    unique_tags = sorted(set(tags))  # Convert to set to get unique tags, then sort in lexicographical order
    return ['<' + tag + '>' for tag in unique_tags]  # Return tags in their opening form