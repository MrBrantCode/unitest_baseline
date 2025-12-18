"""
QUESTION:
Write a function `countTagOccurrences(html, tag)` that takes two parameters: 
- `html`: a string representing the HTML content.
- `tag`: a string representing the HTML tag for which occurrences need to be counted.
 
The function should return the total number of occurrences of the specified HTML tag within the given HTML content.
"""

from html.parser import HTMLParser

class TagCounter(HTMLParser):
    def __init__(self, tag):
        super().__init__()
        self.tag = tag
        self.count = 0

    def handle_starttag(self, tag, attrs):
        if tag == self.tag:
            self.count += 1

def countTagOccurrences(html, tag):
    parser = TagCounter(tag)
    parser.feed(html)
    return parser.count