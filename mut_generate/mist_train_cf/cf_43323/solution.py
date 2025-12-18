"""
QUESTION:
Create a function named `extract_author_info` that takes a string `comment_block` as input and returns a tuple containing the author's name and email. The `comment_block` string is a comment block in the format:
```
 * @package   Storyplayer/Modules/ZeroMQ
 * @author    <NAME> <<EMAIL>>
```
Assuming the input string will always follow this format, with the author's name and email enclosed in angle brackets, extract and return the author's name and email.
"""

import re

def extract_author_info(comment_block: str) -> tuple:
    match = re.search(r'@author\s+(.*?)\s+<(.*?)>', comment_block)
    if match:
        author_name = match.group(1)
        author_email = match.group(2)
        return (author_name, author_email)
    else:
        return ("", "")