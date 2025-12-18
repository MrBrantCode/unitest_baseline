"""
QUESTION:
Design a function called `sort_news_articles` that takes a list of news articles as input and returns the list sorted by most recent. The function should ignore any irrelevant information. The input list will contain dictionaries representing individual news articles, each with a 'timestamp' key representing the article's publication time. The function should return the sorted list of articles in descending order of their timestamps.
"""

def sort_news_articles(news_articles):
    """
    Sorts a list of news articles by their timestamps in descending order.

    Args:
        news_articles (list): A list of dictionaries representing individual news articles.
            Each dictionary should contain a 'timestamp' key.

    Returns:
        list: The sorted list of news articles.
    """
    return sorted(news_articles, key=lambda x: x['timestamp'], reverse=True)