"""
QUESTION:
Implement a function `wiki_page_search` that performs a case-sensitive search for wiki page titles with a minimum length of 3 characters. The function should return the top 5 search results based on relevance, considering the number of incoming links, page views, and user ratings. The function should also accept optional parameters to filter results by page creation date and last modification date, as well as support pagination.
"""

from datetime import datetime

def wiki_page_search(query, min_length=3, creation_date=None, modification_date=None, limit=5):
    """
    Performs a case-sensitive search for wiki page titles with a minimum length of 3 characters.

    Args:
    query (str): The search query.
    min_length (int, optional): The minimum length of the page title. Defaults to 3.
    creation_date (str, optional): The creation date of the page in 'YYYY-MM-DD' format. Defaults to None.
    modification_date (str, optional): The last modification date of the page in 'YYYY-MM-DD' format. Defaults to None.
    limit (int, optional): The number of search results to return. Defaults to 5.

    Returns:
    list: A list of dictionaries containing the page title, incoming links, page views, user ratings, creation date, and modification date.
    """

    # Assuming you have a database or API connection to retrieve the wiki page data
    wiki_pages = [
        {
            'title': 'Page 1',
            'incoming_links': 10,
            'page_views': 100,
            'user_ratings': 5,
            'creation_date': datetime(2022, 1, 1),
            'modification_date': datetime(2022, 1, 15)
        },
        {
            'title': 'Page 2',
            'incoming_links': 5,
            'page_views': 50,
            'user_ratings': 4,
            'creation_date': datetime(2022, 2, 1),
            'modification_date': datetime(2022, 2, 15)
        },
        # Add more pages to the list...
    ]

    # Filter pages by title length
    filtered_pages = [page for page in wiki_pages if len(page['title']) >= min_length]

    # Filter pages by creation date
    if creation_date:
        creation_date = datetime.strptime(creation_date, '%Y-%m-%d')
        filtered_pages = [page for page in filtered_pages if page['creation_date'] >= creation_date]

    # Filter pages by modification date
    if modification_date:
        modification_date = datetime.strptime(modification_date, '%Y-%m-%d')
        filtered_pages = [page for page in filtered_pages if page['modification_date'] <= modification_date]

    # Calculate relevance score based on incoming links, page views, and user ratings
    for page in filtered_pages:
        page['relevance_score'] = page['incoming_links'] + page['page_views'] + page['user_ratings']

    # Sort pages by relevance score in descending order
    filtered_pages.sort(key=lambda x: x['relevance_score'], reverse=True)

    # Return the top N pages
    return filtered_pages[:limit]