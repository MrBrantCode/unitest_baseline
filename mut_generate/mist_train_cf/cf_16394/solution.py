"""
QUESTION:
Implement a function `filter_articles` that categorizes news articles based on their topics. The function should exclude articles about politics, sports, and entertainment, but include articles about technology and science. The articles are represented as strings, and the topics are denoted by specific keywords: 'politics', 'sports', 'entertainment', 'technology', and 'science'.
"""

def filter_articles(article):
    """
    This function filters news articles based on their topics.

    Args:
        article (str): A string representing a news article.

    Returns:
        bool: True if the article is about technology or science, False otherwise.
    """

    # Define the keywords for excluded topics
    excluded_topics = ['politics', 'sports', 'entertainment']

    # Define the keywords for included topics
    included_topics = ['technology', 'science']

    # Check if the article contains any of the excluded topics
    if any(topic in article.lower() for topic in excluded_topics):
        return False

    # Check if the article contains any of the included topics
    if any(topic in article.lower() for topic in included_topics):
        return True

    # If the article does not contain any of the included topics, return False
    return False