"""
QUESTION:
Implement a function `filter_news` that takes a list of news articles and a list of categories as input and returns a filtered list of news articles based on the selected categories. The news articles are represented as dictionaries with keys 'title', 'category', and 'link'. The categories list contains the preferred categories selected by the user.
"""

def filter_news(news_articles, categories):
    """
    Filter news articles based on selected categories.

    Args:
        news_articles (list): A list of news articles, where each article is a dictionary with keys 'title', 'category', and 'link'.
        categories (list): A list of preferred categories selected by the user.

    Returns:
        list: A filtered list of news articles.
    """
    filtered_articles = [article for article in news_articles if article['category'] in categories]
    return filtered_articles