"""
QUESTION:
Implement the `url_for` function to take a route name and optional parameters, and return the corresponding URL. The function should support both simple routes and routes with parameters. Additionally, implement a `test_client.get` function to simulate a GET request to a specified URL and return the response object, ensuring a response status of 200 for successful requests. Assume a basic Flask application with routes already set up.
"""

def url_for(route, **kwargs):
    routes = {
        'index': '/',
        'about': '/about',
        'static': '/{name}/{filename}'
    }
    return routes[route].format(**kwargs)