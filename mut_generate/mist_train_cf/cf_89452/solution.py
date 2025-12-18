"""
QUESTION:
Create a function named `parse_html` that takes an HTML string as input and returns a list of dictionaries, each containing the attributes and content of a `<p>` tag. The function should remove any nested HTML tags within the content of the `<p>` tags and handle nested `<p>` tags correctly. The attributes should be returned as a string.
"""

import re

def parse_html(html):
    pattern = r'<p([^>]*)>(.*?)</p>'
    matches = re.findall(pattern, html, flags=re.DOTALL)
    
    parsed_tags = []
    
    for match in matches:
        tag_attributes = match[0]
        tag_content = match[1]
        
        tag_content = re.sub('<.*?>', '', tag_content)
        
        parsed_tag = {
            'attributes': tag_attributes,
            'content': tag_content
        }
        
        parsed_tags.append(parsed_tag)
    
    return parsed_tags