"""
QUESTION:
Write a function `ignore_search_engine_hits` that filters out hits from web crawlers and search engines to keep accurate view counts. The function should take a request object as input and return True if the hit is from a human, False otherwise.
"""

def ignore_search_engine_hits(request):
    """
    Filters out hits from web crawlers and search engines to keep accurate view counts.
    
    Args:
    request: The HTTP request object.
    
    Returns:
    bool: True if the hit is from a human, False otherwise.
    """
    
    # Define a list of known bot User-Agents
    bot_user_agents = ['Googlebot', 'Bingbot', 'Slurp', 'DuckDuckBot', 'Baiduspider', 'YandexBot']
    
    # Check if the User-Agent is present in the request headers
    if 'User-Agent' in request.headers:
        # Check if the User-Agent matches any known bot
        if any(bot in request.headers['User-Agent'] for bot in bot_user_agents):
            return False
    
    # If no bot User-Agent is found, assume it's a human
    return True