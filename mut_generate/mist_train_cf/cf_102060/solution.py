"""
QUESTION:
Create a function `searchArticles` that takes no parameters. This function should be triggered on every key press in the search input field and should filter a list of articles based on their titles. The search should be case-insensitive and return all articles that contain the search query in their titles. The search results should be dynamically displayed on the page without refreshing the whole page.

Additionally, the function `confirmLeave` should be called when a user clicks on an article link, asking for confirmation before leaving the current page.
"""

def search_articles(search_query, articles):
    """
    Filters a list of articles based on their titles.

    Args:
        search_query (str): The search query to filter articles by.
        articles (list): A list of articles.

    Returns:
        list: A list of articles that contain the search query in their titles.
    """
    # Convert the search query to lowercase for case-insensitive search
    search_query = search_query.lower()
    
    # Initialize an empty list to store the filtered articles
    filtered_articles = []
    
    # Iterate over each article in the list of articles
    for article in articles:
        # Get the title of the article
        title = article.get('title', '').lower()
        
        # Check if the title contains the search query
        if search_query in title:
            # If the title contains the search query, add the article to the filtered list
            filtered_articles.append(article)
    
    # Return the filtered list of articles
    return filtered_articles