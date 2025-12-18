"""
QUESTION:
Create a function named `parse_html` that takes a string of HTML as input and returns a list of dictionaries, where each dictionary represents a <p> tag and contains two keys: 'attributes' and 'content'. The 'attributes' key stores the attributes of the <p> tag as a string, and the 'content' key stores the content of the <p> tag with any nested HTML tags removed. The function should handle nested <p> tags correctly.
"""

import re

def parse_html(html):
    pattern = r'<p([^>]*)>(.*?)</p>'
    matches = re.findall(pattern, html)

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