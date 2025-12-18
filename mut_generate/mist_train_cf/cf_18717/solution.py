"""
QUESTION:
Write a function named `determine_language(html)` that determines the language used to write an HTML document. The function should take a string `html` representing the HTML document as input and return the identified language as a string. 

If multiple language declarations are present in the HTML document, consider the order of precedence: `<meta>` tag, `<html>` tag, `<head>` tag. If no explicit language declaration is found, analyze the content to make an educated guess about the language. Do not use any external libraries or pre-built language detection tools.
"""

import re

def determine_language(html):
    language = re.search(r'<meta[^>]*http-equiv=[^>]*content=[\'"]*[^>]*charset=([^\'">]*)', html)
    if language:
        return language.group(1).split('-')[0]
    
    language = re.search(r'<(?:html|head)[^>]*lang=[\'"]*([^\'">]*)', html)
    if language:
        return language.group(1)
    
    text_content_match = re.search(r'<body[^>]*>(.*)</body>', html, re.DOTALL)
    if text_content_match:
        body_content = text_content_match.group(1)
        text_content = re.sub(r'<[^>]*>', '', body_content).strip()
        
        # Add your own language analysis logic here
        # This is just a placeholder example
        if 'こんにちは' in text_content:
            return 'Japanese'
        elif 'مرحبا' in text_content:
            return 'Arabic'
    
    return 'Language could not be determined.'