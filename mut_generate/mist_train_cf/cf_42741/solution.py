"""
QUESTION:
Implement a function `count_html_tags(html_snippet: str) -> dict` that takes an HTML snippet string of length between 1 and 10^5 as input, parses it, and returns a dictionary containing the count of each HTML tag present in the snippet. The keys in the dictionary should be the HTML tag names, and the values should be the counts of each tag.
"""

from html.parser import HTMLParser

class TagCounter(HTMLParser):
    def __init__(self):
        super().__init__()
        self.tag_counts = {}

    def handle_starttag(self, tag, attrs):
        self.tag_counts[tag] = self.tag_counts.get(tag, 0) + 1

def count_html_tags(html_snippet: str) -> dict:
    parser = TagCounter()
    parser.feed(html_snippet)
    return parser.tag_counts