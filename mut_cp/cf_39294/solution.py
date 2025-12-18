"""
ORIGINAL QUESTION:
Write a function `parse_code_snippet(code)` that takes a string `code` as input, extracts the author's name, date, and the lower range of GitHub stars from the comments section, and returns a tuple `(author_name, date, gh_stars)`. The function should use a specific comment format:
```
# @Author: <author_name>
# @Date  : <date>
# <gh_stars>-<gh_stars>
```
The function should return `None` if the pattern is not found in the code snippet.
"""

import re

def parse_code_snippet(code):
    pattern = r'# @Author: (.+)\n# @Date  : (.+)\n# (\d+)-\d+'
    match = re.search(pattern, code)
    if match:
        author_name = match.group(1)
        date = match.group(2)
        gh_stars = int(match.group(3))
        return (author_name, date, gh_stars)
    else:
        return None