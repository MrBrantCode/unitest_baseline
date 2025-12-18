"""
QUESTION:
Create a function named `html_to_json(html_string)` that takes a string representing an HTML document as input and returns a JSON object representing the structure of the HTML document. 

Each tag in the HTML document should be represented as an object with a "tag" property and a "children" property. If a tag has no children, the "children" property should be an empty array. If a tag contains only text content, it should be represented as an object with a "type" property set to "text" and a "content" property containing the text content.

Assume the input HTML document is valid and properly formatted, with balanced opening and closing tags.
"""

import json
from html.parser import HTMLParser

class HTMLToJsonParser(HTMLParser):
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
    parser = HTMLToJsonParser()
    parser.feed(html_string)
    return json.dumps(parser.json_structure, indent=2)