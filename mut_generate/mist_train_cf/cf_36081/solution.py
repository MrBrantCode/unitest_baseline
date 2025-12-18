"""
QUESTION:
Write a function `extractMetadata` that takes a string `source_code` as input and returns a dictionary containing metadata information extracted from a comment block in the source code. The comment block starts with `/**` and ends with `*/`, and metadata tags are denoted by `@` followed by the tag name, with values provided after the tag name. Each tag and its value are separated by a space.
"""

import re

def extractMetadata(source_code: str) -> dict:
    metadata = {}
    comment_block = re.search(r'/\*\*(.*?)\*/', source_code, re.DOTALL)
    if comment_block:
        tags = re.findall(r'@(\w+)\s(.*?)\n', comment_block.group(1))
        for tag, value in tags:
            metadata[tag] = value.strip()
    return metadata