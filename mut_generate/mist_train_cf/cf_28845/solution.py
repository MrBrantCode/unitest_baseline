"""
QUESTION:
Implement a function `get_articles(category)` that takes a category as input and returns a list of articles related to that category. The function should return an empty list if the category does not exist. 

The articles data is a dictionary where the keys are categories and the values are lists of articles. Each article is a dictionary with 'title' and 'content' keys. 

Write the `get_articles` function to retrieve articles from the articles data based on the specified category.
"""

def get_articles(category, all_articles):
    """
    Retrieves articles from the articles data based on the specified category.

    Args:
        category (str): The category of articles to retrieve.
        all_articles (dict): A dictionary containing articles data.

    Returns:
        list: A list of articles related to the specified category.
    """
    return all_articles.get(category, [])