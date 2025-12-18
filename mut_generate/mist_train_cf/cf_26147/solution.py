"""
QUESTION:
Create a function to aggregate news from multiple sources and filter the news items based on topics, sources, and titles. The function should return the filtered news items. 

The function should be named `aggregate_news` and it should accept a list of news sources and a dictionary of filter parameters (topics, sources, titles).
"""

def aggregate_news(sources, filters):
    """
    Aggregate news from multiple sources and filter the news items based on topics, sources, and titles.

    Args:
        sources (list): A list of news sources.
        filters (dict): A dictionary of filter parameters (topics, sources, titles).

    Returns:
        list: The filtered news items.
    """

    # Initialize an empty list to store filtered news items
    filtered_news = []

    # Iterate over each news source
    for source in sources:
        # Extract news items from the source
        news_items = source.get('items', [])

        # Iterate over each news item
        for item in news_items:
            # Check if the item matches the filter criteria
            if (
                ('topics' not in filters or item.get('topic') in filters['topics']) and
                ('sources' not in filters or source.get('name') in filters['sources']) and
                ('titles' not in filters or item.get('title') in filters['titles'])
            ):
                # Add the item to the filtered news list
                filtered_news.append(item)

    # Return the filtered news items
    return filtered_news