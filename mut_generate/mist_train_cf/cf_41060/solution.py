"""
QUESTION:
Create a function `extractArticles(htmlContent)` that takes a string of HTML code as input and returns a list of dictionaries. The input string contains multiple articles, each enclosed within `<a>` tags with a title enclosed within `<h2>` tags and content enclosed within `<p>` tags. The function should extract the title and content of each article and return them as a list of dictionaries in the format `[{'title': 'title', 'content': 'content'}, ...]`. If no articles are found, an empty list should be returned.
"""

import re

def extractArticles(htmlContent):
    articles = re.findall(r'<a>.*?<h2>(.*?)</h2>.*?<p>(.*?)</p>.*?</a>', htmlContent, re.DOTALL)
    extracted_articles = [{'title': title, 'content': content} for title, content in articles]
    return extracted_articles