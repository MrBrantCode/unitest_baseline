"""
QUESTION:
Implement a function `extract_text_from_html` that takes two parameters: `html_string` and `tags`. The function should return a list of strings containing the text content of the specified tags in the order they appear in the HTML string. If the `tags` parameter is empty or None, all tags should be considered. The function should ignore attributes within the tags, handle arbitrary depth of nested elements, treat self-closing tags as if they have no text content, convert special characters within the text content back to their corresponding characters, and have a time complexity of O(N + M), where N is the length of the HTML string and M is the number of HTML elements that match the specified tags.
"""

from html.parser import HTMLParser

def extract_text_from_html(html_string, tags):
    class TextExtractor(HTMLParser):
        def __init__(self, tags=None):
            super().__init__()
            self.tags = tags
            self.result = []
            self.current_tag = None

        def handle_starttag(self, tag, attrs):
            if not self.tags or tag in self.tags:
                self.current_tag = tag

        def handle_data(self, data):
            if self.current_tag:
                self.result.append(data.strip())

        def handle_endtag(self, tag):
            if self.current_tag == tag:
                self.current_tag = None

    parser = TextExtractor(tags)
    parser.feed(html_string)
    return parser.result