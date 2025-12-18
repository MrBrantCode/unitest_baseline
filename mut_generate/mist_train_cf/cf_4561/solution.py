"""
QUESTION:
Write a function `extract_font_styles` that takes a string representing an HTML document and returns a set of font style names available within the document. 

The function should consider the following font style tags: `<b>`, `<i>`, `<u>`, `<s>`, `<strong>`, `<em>`, `<ins>`, `<del>`. It should ignore font style tags within comments or script/style blocks, handle nested tags and tags with attributes, and identify tags regardless of case. The function should return a set of unique font style names.
"""

import re

def extract_font_styles(html):
    pattern = r'<(b|i|u|s|strong|em|ins|del)[^>]*?>'

    font_styles = set()

    html = re.sub(r'<!--.*?-->', '', html, flags=re.DOTALL)
    html = re.sub(r'<script.*?</script>', '', html, flags=re.DOTALL)
    html = re.sub(r'<style.*?</style>', '', html, flags=re.DOTALL)

    matches = re.findall(pattern, html, flags=re.IGNORECASE)

    for match in matches:
        font_style = re.sub(r'<|>', '', match).lower()

        font_styles.add(font_style)

    return font_styles