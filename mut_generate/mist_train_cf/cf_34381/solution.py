"""
QUESTION:
Implement the `authenticated` decorator function to restrict access to a method based on user authentication. The function should take a method as input, check the user's authentication status, and either allow the method to proceed or return an error response if the user is not authenticated.

The `authenticated` decorator should be applied to a method that returns a JSON response with a success message if the user is authenticated and a JSON response with an error message if the user is not authenticated. The user's authentication status is determined by a predefined authentication mechanism, such as username/password, token, or session. Assume that the authentication status is available as a boolean flag (e.g., `self.current_user`).

The decorator should return a JSON response with a success message `{"msg": "Success"}` if the user is authenticated and a JSON response with an error message `{"error": "Unauthorized"}` and a 401 status code if the user is not authenticated.
"""

import functools

def authenticated(method):
    @functools.wraps(method)
    def wrapper(self, *args, **kwargs):
        if self.current_user:
            return method(self, *args, **kwargs)
        else:
            self.set_status(401)  # Unauthorized status code
            self.write({"error": "Unauthorized"})
    return wrapper