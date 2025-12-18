"""
QUESTION:
Implement the `handle_request` function to handle HTTP requests and respond with appropriate HTTP responses for the given routes and methods.

The `handle_request` function should take two parameters: `method` (the HTTP method) and `path` (the endpoint URL). It should return a tuple containing the HTTP status code and the corresponding content.

The function should support the following HTTP methods: GET, POST, PUT, DELETE and handle the following status codes: 200 OK, 404 Not Found, 405 Method Not Allowed. 

The function should handle the following routes: "/", "/about", "/contact" with the corresponding content. For each route, the function should handle the HTTP methods as follows: 
- GET: Retrieve the content for the specified route.
- POST: Create new content for the specified route.
- PUT: Update the content for the specified route.
- DELETE: Delete the content for the specified route.

The function should handle invalid routes and methods by returning appropriate error responses.

The routes and their corresponding content should be stored in a dictionary, where the keys are the endpoint URLs and the values are the corresponding content.
"""

def handle_request(method, path):
    """
    Handles HTTP requests and responds with appropriate HTTP responses for the given routes and methods.

    Args:
    method (str): The HTTP method.
    path (str): The endpoint URL.

    Returns:
    tuple: A tuple containing the HTTP status code and the corresponding content.
    """
    routes = {
        "/": "Welcome to the server!",
        "/about": "This is a simple web server.",
        "/contact": "Contact us at example@email.com"
    }

    if path in routes:
        if method == "GET":
            return "200 OK", routes[path]
        elif method == "POST":
            routes[path] = "New content created"
            return "200 OK", "Content created successfully"
        elif method == "PUT":
            routes[path] = "Content updated"
            return "200 OK", "Content updated successfully"
        elif method == "DELETE":
            del routes[path]
            return "200 OK", "Content deleted successfully"
        else:
            return "405 Method Not Allowed", "Method not allowed for this route"
    else:
        return "404 Not Found", "Route not found"