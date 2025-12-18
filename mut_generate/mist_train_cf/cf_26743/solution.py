"""
QUESTION:
Create a function `find_view` that takes a URL string as input and returns the name of the corresponding view function based on the provided URL patterns.

The URL patterns are defined using Python's Django URL syntax and are unique without overlaps. The function should match the input URL with the URL patterns and return the name of the view function. If no match is found, it should return "Not Found".

The function should work with the given list of URL patterns: 
    - `r'^users$'` maps to "index"
    - `r'^users/(?P<id>\d+)$'` maps to "show"
    - `r'^users/new$'` maps to "new"
    - `r'^users/create$'` maps to "create"
    - `r'^users/(?P<id>\d+)/edit$'` maps to "edit"
    - `r'^users/(?P<id>\d+)/delete$'` maps to "delete"
    - `r'^users/(?P<id>\d+)/update$'` maps to "update"
"""

import re

def find_view(url: str) -> str:
    """
    This function takes a URL string as input and returns the name of the corresponding view function.
    
    Args:
    url (str): The input URL string.
    
    Returns:
    str: The name of the corresponding view function or "Not Found" if no match is found.
    """
    
    urlpatterns = [
        (r'^users$', 'index'),
        (r'^users/(?P<id>\d+)$', 'show'),
        (r'^users/new$', 'new'),
        (r'^users/create$', 'create'),
        (r'^users/(?P<id>\d+)/edit$', 'edit'),
        (r'^users/(?P<id>\d+)/delete$', 'delete'),
        (r'^users/(?P<id>\d+)/update$', 'update')
    ]
    
    for pattern in urlpatterns:
        if re.match(pattern[0], url):
            return pattern[1]
    return "Not Found"