"""
QUESTION:
Write a function named `find_font_styles` that takes a string representing an HTML document and returns a set of font styles found in the document. The function should consider the following font style tags: <b>, <i>, <u>, <s>, <strong>, <em>, <ins>, <del>, and handle their variations (uppercase or mixed case tags). It should ignore font style tags within comments, script, or style blocks, and only count nested font style tags once.
"""

import re

def find_font_styles(html):
    # Remove comments and script/style blocks
    html = re.sub(r"<!--.*?-->", "", html, flags=re.DOTALL)
    html = re.sub(r"<script.*?</script>", "", html, flags=re.DOTALL)
    html = re.sub(r"<style.*?</style>", "", html, flags=re.DOTALL)

    # Find all font style tags
    font_style_tags = re.findall(r"<(b|i|u|s|strong|em|ins|del)>", html, flags=re.IGNORECASE)

    # Remove duplicates and convert to lowercase
    font_styles = set(map(str.lower, font_style_tags))

    return font_styles