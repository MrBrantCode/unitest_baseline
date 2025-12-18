"""
QUESTION:
Write a function `parse_webpage` to fetch webpages from a given website using the Scrapy framework in Python. The function should take a URL as input and return the title, link, and content of each webpage. The function should be able to extract the structured data from webpages, handle different types of webpages, and respect the website's robots.txt rules and terms of service.
"""

def parse_webpage(response):
    title = response.css('h1.entry-title::text').extract()[0]
    link = response.url
    content = response.css('div.entry-content').extract()[0]
    return {
        'title': title,
        'link': link,
        'content': content
    }