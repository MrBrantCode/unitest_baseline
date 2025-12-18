"""
QUESTION:
Create a function `extract_h3_tags(html)` that takes an HTML string as input, extracts all the <h3> tags along with their corresponding text content, removes any HTML tags within the extracted text content, and returns a list of objects containing the heading as "heading" and the corresponding text content as "text". If a <h3> tag does not have any adjacent text content, the "text" field should be an empty string. The function should also handle nested <h3> tags by including all the nested content.
"""

import re

def extract_h3_tags(html):
    # Find all <h3> tags and their corresponding text content using regex
    h3_tags = re.findall(r'<h3>(.*?)</h3>', html, re.DOTALL)
    
    extracted_tags = []
    for tag in h3_tags:
        # Remove any HTML tags within the extracted text content
        text = re.sub(r'<.*?>', '', tag)
        
        # Remove leading and trailing whitespace from the text content
        text = text.strip()
        
        # Add the extracted tag to the list
        extracted_tags.append({
            "heading": tag,
            "text": text
        })
    
    return extracted_tags