"""
QUESTION:
Implement a URL routing system with four endpoints (icons, charts, tables, login) and define the corresponding handler functions. Create a function called `route_request(url, request)` that takes a URL and a request as input, and directs the request to the appropriate handler function based on the requested endpoint. The function should handle invalid endpoints accordingly. 

The handler functions should be named `icons(request)`, `charts(request)`, `tables(request)`, and `login(request)`, each taking a request as input.
"""

def route_request(url, request):
    """
    Directs a request to the appropriate handler function based on the requested endpoint.

    Args:
        url (str): The URL of the incoming request.
        request: The request object.

    Returns:
        The response from the handler function.
    """
    # Define handler functions for each endpoint
    def icons(request):
        # Handler logic for the 'icons' endpoint
        # ...
        pass

    def charts(request):
        # Handler logic for the 'charts' endpoint
        # ...
        pass

    def tables(request):
        # Handler logic for the 'tables' endpoint
        # ...
        pass

    def login(request):
        # Handler logic for the 'login' endpoint
        # ...
        pass

    # URL routing logic
    if url.startswith('/icon'):
        return icons(request)
    elif url.startswith('/chart'):
        return charts(request)
    elif url.startswith('/table'):
        return tables(request)
    elif url.startswith('/log'):
        return login(request)
    else:
        # Handle invalid endpoint
        # ...
        pass