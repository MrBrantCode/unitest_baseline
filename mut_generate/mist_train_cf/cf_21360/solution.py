"""
QUESTION:
Create a function called `parse_html` that takes a string of HTML as input and returns a list of all class names found in the HTML. The function should handle nested HTML elements and should not use any external libraries or frameworks other than the Python standard library.
"""

from html.parser import HTMLParser

class ClassParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.classes = []

    def handle_starttag(self, tag, attrs):
        class_attr = dict(attrs).get('class')
        if class_attr:
            self.classes.extend(class_attr.split())

def parse_html(html_string):
    parser = ClassParser()
    parser.feed(html_string)
    return parser.classes