"""
QUESTION:
Write a function `extract_font_styles` that takes a string `html` representing an HTML document as input and returns a set of unique font style names found in the document. The function should consider the following font style tags: `<b>`, `<i>`, `<u>`, `<s>`, `<strong>`, `<em>`, `<ins>`, `<del>`. It should ignore font style tags within comments or within a script or style block, handle nested tags, and variations of the font style tags, such as uppercase or mixed case tags. The function should also handle cases where font style tags have attributes other than just the tag name and cases where font style tags are not properly closed.
"""

import re

def extract_font_styles(html):
    # Regular expression pattern to match font style tags
    pattern = r'<(b|i|u|s|strong|em|ins|del)[^>]*?>'

    # Set to store unique font styles
    font_styles = set()

    # Remove comments and script/style blocks from the HTML
    html = re.sub(r'<!--.*?-->', '', html, flags=re.DOTALL)
    html = re.sub(r'<script.*?</script>', '', html, flags=re.DOTALL)
    html = re.sub(r'<style.*?</style>', '', html, flags=re.DOTALL)

    # Extract font styles from the remaining HTML
    matches = re.findall(pattern, html, flags=re.IGNORECASE)

    for match in matches:
        # Extract font style name from the tag
        font_style = re.sub(r'<|>', '', match).lower()

        # Add font style to the set
        font_styles.add(font_style)

    return font_styles