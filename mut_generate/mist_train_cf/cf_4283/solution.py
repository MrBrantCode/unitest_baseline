"""
QUESTION:
Implement a function `extract_h1_tags` that takes a string `html` representing a nested HTML page and returns a list of text content of all `<h1>` tags and the total number of characters in the extracted text content. The function should handle HTML pages with multiple nested tags and arbitrary nesting levels, and its time complexity should be less than or equal to O(n), where n is the total number of characters in the input HTML page. The space complexity should be less than or equal to O(m), where m is the total number of `<h1>` tags in the input HTML page.
"""

from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.h1_tags = []
        self.total_chars = 0
    
    def handle_starttag(self, tag, attrs):
        if tag == 'h1':
            self.h1_tags.append('')
    
    def handle_endtag(self, tag):
        if tag == 'h1':
            self.total_chars += len(self.h1_tags[-1])
    
    def handle_data(self, data):
        if len(self.h1_tags) > 0:
            self.h1_tags[-1] += data
    
    def extract_h1_tags(self, html):
        self.feed(html)
        return self.h1_tags, self.total_chars

def extract_h1_tags(html):
    parser = MyHTMLParser()
    return parser.extract_h1_tags(html)