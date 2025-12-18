"""
QUESTION:
Create a function `markdownToHTML(markdown: str) -> str` that takes a string of Markdown text as input and returns the corresponding HTML string. The function should support the conversion of Markdown headers (lines starting with one or more `#` characters followed by a space) to HTML headers, and the conversion of text enclosed within double asterisks `**` to HTML bold tags and text enclosed within single asterisks `*` to HTML italics tags.
"""

import re

def markdownToHTML(markdown: str) -> str:
    # Convert headers
    markdown = re.sub(r'^(#+)\s(.*)$', lambda match: f'<h{len(match.group(1))}>{match.group(2)}</h{len(match.group(1))}>', markdown, flags=re.MULTILINE)
    
    # Convert bold text
    markdown = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', markdown)
    
    # Convert italic text
    markdown = re.sub(r'\*(.*?)\*', r'<em>\1</em>', markdown)
    
    return markdown