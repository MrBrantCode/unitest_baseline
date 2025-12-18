"""
QUESTION:
Implement a function `fileapp` that defines a WSGI application to serve a static file. The application should accept two parameters: `environ` and `start_response`. It should return a simple HTML page with the content "<html><body><h1>Hello, World!</h1></body></html>". The `start_response` function should be called with the status '200 OK' and a header specifying the content type as 'text/html; charset=utf-8'. The function should not take any command-line arguments.
"""

def fileapp(environ, start_response):
    """
    Defines a WSGI application to serve a static file.

    Args:
        environ: WSGI environment.
        start_response: WSGI response function.

    Returns:
        A simple HTML page with the content "<html><body><h1>Hello, World!</h1></body></html>".
    """
    status = '200 OK'
    headers = [('Content-type', 'text/html; charset=utf-8')]
    start_response(status, headers)
    return [b"<html><body><h1>Hello, World!</h1></body></html>"]