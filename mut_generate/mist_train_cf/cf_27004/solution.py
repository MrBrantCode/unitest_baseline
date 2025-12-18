"""
QUESTION:
Create a function `extract_file_info` that takes a string `input_string` as its parameter. The input string will be in the format `<reponame><author_username>/<repository_name><filename><file_name>`. The function should return a dictionary containing the extracted information with the keys `repository_name`, `author_username`, and `file_name`.
"""

import re

def extract_file_info(input_string):
    match = re.match(r'<reponame>(?P<author_username>[\w-]+)/(?P<repository_name>[\w-]+)<filename>(?P<file_name>.+)', input_string)
    if match:
        return {
            'repository_name': match.group('repository_name'),
            'author_username': match.group('author_username'),
            'file_name': match.group('file_name')
        }
    else:
        return None