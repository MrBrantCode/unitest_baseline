"""
QUESTION:
Implement a `BaseNewsQuerySet` class with a method `published()` that filters the query set to return only news articles with a `publication_status` of 'published'.
"""

def published(news_articles):
    return [article for article in news_articles if article['publication_status'] == 'published']