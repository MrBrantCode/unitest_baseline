"""
QUESTION:
Create a function `generate_tag_suffix(branch, tag, tag_regex)` that generates a tag suffix based on the input parameters. The function takes three parameters: `branch` (string), `tag` (string), and `tag_regex` (regular expression object). 

The function should determine the tag suffix based on the following rules:
- If the `branch` matches the pattern `devel-\d+`, the tag suffix should be '-devel'.
- If the `branch` matches the pattern `master-\d+`, the tag suffix should be '-pre-release'.
- If the `branch` matches the patterns `feature-\d+` or `bugfix-\d+`, the tag suffix should be the extracted branch and number joined by '-' using the `tag_regex`.
- If the `tag` is not empty and starts with 'release/', the tag suffix should be an empty string.
- If none of the above conditions are met, the tag suffix should be '-'.

The function should return the tag suffix as a string.
"""

import re

def generate_tag_suffix(branch: str, tag: str, tag_regex: re.Pattern) -> str:
    if re.match(r'devel-\d+', branch):
        return '-devel'
    elif re.match(r'master-\d+', branch):
        return '-pre-release'
    elif re.match(r'feature-\d+', branch) or re.match(r'bugfix-\d+', branch):
        return '-' + '-'.join(tag_regex.search(branch).groups())
    elif tag and tag.startswith('release/'):
        return ''
    else:
        return '-'