"""
QUESTION:
Implement the `clean_html` function that takes a string `html` as input and returns the processed text according to the following operations: replace `</p>` tags with a newline character `\n`, replace `<br>` or `<br/>` tags with a newline character `\n`, remove all HTML tags by replacing them with a space character, replace consecutive spaces with a single space, and strip leading and trailing whitespace from each line. The function should return a string.
"""

import re

def clean_html(html: str) -> str:
    html = html.replace('</p>', '\n')
    html = re.sub('<br\s*/?>', '\n', html)
    html = re.sub('<.*?>', ' ', html)
    html = re.sub(' +', ' ', html)
    html = '\n'.join([x.strip() for x in html.splitlines()])
    return html.strip()