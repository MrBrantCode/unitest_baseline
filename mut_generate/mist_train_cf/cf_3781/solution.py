"""
QUESTION:
Write a function `html_to_json(html_string)` that takes a string representing a valid and properly formatted HTML document as input and returns a JSON object representing the structure of the HTML document. 

Each tag in the HTML document should be represented as an object with a "tag" property and a "children" property. The "children" property should be an array of child elements or text content, where text content is represented as an object with a "type" property set to "text" and a "content" property containing the text content. If a tag has no children, the "children" property should be an empty array.
"""

import json
from html.parser import HTMLParser

class HTMLParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.stack = []
        self.json_structure = {}

    def handle_starttag(self, tag, attrs):
        node = {"tag": tag, "children": []}
        if self.stack:
            self.stack[-1]["children"].append(node)
        else:
            self.json_structure = node
        self.stack.append(node)

    def handle_endtag(self, tag):
        self.stack.pop()

    def handle_data(self, data):
        if self.stack:
            self.stack[-1]["children"].append({"type": "text", "content": data.strip()})

def html_to_json(html_string):
    parser = HTMLParser()
    parser.feed(html_string)
    return json.dumps(parser.json_structure, indent=2)