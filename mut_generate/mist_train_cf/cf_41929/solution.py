"""
QUESTION:
Write a function `extractHTMLComments` that takes a string representing the content of an HTML file as input and returns a list of strings, where each string represents an extracted HTML comment. The input HTML content is well-formed and valid, and HTML comments will not be nested within each other.
"""

import re

def extractHTMLComments(html_content):
    comment_pattern = r'<!--(.*?)-->'
    comments = re.findall(comment_pattern, html_content, re.DOTALL)
    return [comment.strip() for comment in comments]