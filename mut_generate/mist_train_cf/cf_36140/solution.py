"""
QUESTION:
Write a function `countHTMLComments` that takes a string of HTML content as input and returns the total count of HTML comments present in the string. An HTML comment is defined as any text enclosed within `<!--` and `-->`. The function should be able to handle multiple HTML comments and return the total count.
"""

import re

def countHTMLComments(html_content):
    comment_pattern = r'<!--(.*?)-->'
    comments = re.findall(comment_pattern, html_content, re.DOTALL)
    return len(comments)