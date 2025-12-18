"""
QUESTION:
Create a function `generate_login_link` that takes a `request` object as input and returns the login link for the Shibboleth login page as a string. The `request` object is assumed to contain the necessary information to construct the login link, including the `build_absolute_uri` method to get the absolute URL of the current request.
"""

def generate_login_link(request) -> str:
    shibboleth_login_url = "https://example.com/shibboleth-login"
    return_url = request.build_absolute_uri()
    login_link = f"{shibboleth_login_url}?return={return_url}"
    return login_link