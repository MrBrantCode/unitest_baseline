"""
QUESTION:
Implement a function called `parse_commit_message` that takes a commit message as input and returns a dictionary containing the author name, author email, service name, tag, and environment. The commit message is expected to be in a specific format with each detail on a new line, prefixed with 'Author: ', 'Service: ', 'Tag: ', and 'Environment: ' respectively. If the input message does not match the expected format, the function should return None.
"""

import re

def parse_commit_message(message):
    pattern = r'Author: (.+?) <(.+?)>\nService: (.+?)\nTag: (.+?)\nEnvironment: (.+)'
    match = re.search(pattern, message, re.MULTILINE)
    
    if match:
        author_name = match.group(1)
        author_email = match.group(2)
        service_name = match.group(3)
        tag = match.group(4)
        env = match.group(5)
        
        return {
            'author_name': author_name,
            'author_email': author_email,
            'service_name': service_name,
            'tag': tag,
            'environment': env
        }
    else:
        return None