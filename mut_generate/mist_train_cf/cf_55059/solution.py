"""
QUESTION:
Implement a function called `sanitize_html` that takes a string of HTML content as input, removes any malicious script tags, and returns the sanitized HTML content. The function should prevent Cross-site Scripting (XSS) attacks by removing any executable scripts from the input HTML.
"""

import re

def sanitize_html(html_content):
    """
    Sanitizes the input HTML content by removing any malicious script tags.

    Args:
        html_content (str): The input HTML content.

    Returns:
        str: The sanitized HTML content.
    """
    # Use regular expression to remove script tags
    sanitized_content = re.sub(r'<script.*?>.*?<\/script>', '', html_content, flags=re.DOTALL)
    
    return sanitized_content