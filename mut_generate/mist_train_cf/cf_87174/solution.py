"""
QUESTION:
Write a function named `count_special_classes` that takes a string representing an HTML document as input and returns the number of times the word "special" appears as a class for any heading element (h1 to h6) that is located inside a div element with the id "container". The function should have a time complexity of O(n), where n is the length of the input string, and a space complexity of O(1).
"""

import re

def count_special_classes(html):
    count = 0
    pattern = r'<div id="container">.*?</div>'
    container_match = re.search(pattern, html, re.DOTALL)
    if container_match:
        container_html = container_match.group(0)
        headings = re.findall(r'<h[1-6][^>]*class="[^"]*special[^"]*"[^>]*>.*?</h[1-6]>', container_html, re.DOTALL)
        count = len(headings)
    return count