"""
QUESTION:
Implement the function `countNestedElements(html: str, tagName: str) -> int`, which takes in an HTML document as a string and a tag name as parameters. The function should parse the HTML document and return the count of nested HTML elements within the specified tag.
"""

from html.parser import HTMLParser

class TagCounter(HTMLParser):
    def __init__(self, tag_name):
        super().__init__()
        self.tag_name = tag_name
        self.count = 0
        self.inside_target_tag = False

    def handle_starttag(self, tag, attrs):
        if tag == self.tag_name:
            self.inside_target_tag = True
        if self.inside_target_tag and tag != self.tag_name:
            self.count += 1

    def handle_endtag(self, tag):
        if tag == self.tag_name:
            self.inside_target_tag = False

def countNestedElements(html: str, tagName: str) -> int:
    parser = TagCounter(tagName)
    parser.feed(html)
    return parser.count