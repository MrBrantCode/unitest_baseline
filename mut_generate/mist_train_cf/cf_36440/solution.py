"""
QUESTION:
Write a function `process_stream(stream: str, pattern: str) -> str` that takes a string `stream` and a regular expression pattern `pattern`. The function should process the `stream` based on the matches found using the `pattern`, and return the modified string `ans`. For each match found, if it starts with "<", append the entire match to `ans`. Otherwise, split the match into individual elements, reverse each element, and append the reversed elements separated by a space to `ans`.
"""

import re

def process_stream(stream: str, pattern: str) -> str:
    ans = ""
    p = re.compile(pattern)
    for elem in p.findall(stream):
        if elem[0] == "<":
            ans += elem
        else:
            for e in elem.split():
                ans += e[::-1] + " "
    return ans.strip()