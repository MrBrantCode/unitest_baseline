"""
QUESTION:
Write a function named `extract_h1_tags` that takes an HTML string as input and returns a list of text content of all <h1> tags in the HTML, as well as the total number of characters in the extracted text content. The function should be able to handle HTML pages with arbitrary levels of nesting and should have a time complexity of O(n), where n is the total number of characters in the input HTML page, and a space complexity of O(m), where m is the total number of <h1> tags in the input HTML page.
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
        self.h1_tags = []
        self.total_chars = 0
        self.feed(html)
        return self.h1_tags, self.total_chars

def extract_h1_tags(html):
    parser = MyHTMLParser()
    return parser.extract_h1_tags(html)