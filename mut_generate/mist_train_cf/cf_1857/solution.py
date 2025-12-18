"""
QUESTION:
Write a function called `count_special_classes` that takes in a string representing an HTML document and returns the number of times the word "special" appears as a class for any heading element (h1 to h6) that is located inside a div element with the id "container". The function should have a time complexity of O(n), where n is the length of the input string, and a space complexity of O(1).
"""

import re

def count_special_classes(html):
    count = 0
    pattern = r'<div id="container">.*?</div>'
    container_match = re.search(pattern, html)
    if container_match:
        container_html = container_match.group(0)
        headings = re.findall(r'<h[1-6].*?</h[1-6]>', container_html)
        for heading in headings:
            if 'class="special"' in heading:
                count += 1
    return count