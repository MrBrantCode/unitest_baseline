"""
QUESTION:
Implement a `Router` class that acts as a WSGI middleware to map incoming requests to WSGI apps based on specified routes.

The `Router` class should have the following methods:
- `__init__(self, mapper)`: Initializes the router with a `mapper` object representing the routes.
- `route_request(self, request)`: Routes the incoming request to the appropriate WSGI app based on the specified routes.

Assume the `mapper` object has the necessary routes defined, where each route specifies a 'controller' (a WSGI app to call) and optionally an 'action' to further specify the behavior.
"""

def Router(mapper):
    """WSGI middleware that maps incoming requests to WSGI apps."""

    def route_request(request):
        """Route the incoming request to the appropriate WSGI app based on the specified routes."""
        path_info = request.environ.get('PATH_INFO', '').lstrip('/')
        for route in mapper.match(path_info):
            if route:
                controller = route.pop('controller', None)
                action = route.pop('action', 'index')
                if controller:
                    return controller, action
        return None, None  # If no matching route is found

    return route_request