"""
QUESTION:
Write a classifier to filter articles in a newsreader application. The classifier should only include articles about current world news and exclude articles about politics and sports.
"""

def classify_article(article):
    """
    Classify an article as world news if it does not pertain to politics or sports.

    Args:
        article (dict): A dictionary containing information about the article.

    Returns:
        bool: True if the article is about world news, False otherwise.
    """
    excluded_topics = ['politics', 'sports']
    return article['topic'] not in excluded_topics