"""
QUESTION:
Implement a function `generate_sitemap` that takes a list of blog posts as input and generates an XML sitemap as output. The sitemap should be ordered based on the `view_count` of the posts in descending order. Each post is represented as a dictionary containing `title`, `updated_at`, and `view_count`.

Function Signature:
```python
def generate_sitemap(posts: List[Dict[str, Union[str, int]]]) -> str:
```
The input `posts` is a list of dictionaries where each dictionary contains the following key-value pairs:
- `title`: a string representing the title of the blog post.
- `updated_at`: a string representing the date and time when the blog post was last updated.
- `view_count`: an integer representing the number of views for the blog post.

The output is a string representing the XML sitemap.
"""

from typing import List, Dict, Union

def generate_sitemap(posts: List[Dict[str, Union[str, int]]]) -> str:
    xml_output = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
    for post in sorted(posts, key=lambda x: x['view_count'], reverse=True):
        xml_output += f'    <url>\n        <loc>URL_TO_{post["title"].replace(" ", "_")}</loc>\n'
        xml_output += f'        <lastmod>{post["updated_at"].replace(" ", "T")}:00+00:00</lastmod>\n'
        xml_output += f'        <changefreq>weekly</changefreq>\n'
        xml_output += f'        <priority>{round(post["view_count"] / max([p["view_count"] for p in posts]), 1)}</priority>\n    </url>\n'
    xml_output += '</urlset>'
    return xml_output