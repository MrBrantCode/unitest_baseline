"""
QUESTION:
Implement a Single Sign-On (SSO) system for multiple domains with different authentication methods. The system should allow users to access multiple websites without needing to log in multiple times.

Function: Implement a centralized authentication server to manage user identities and process login requests from different domains. The system should support protocols like SAML, OAuth, OpenID Connect, etc. 

Restrictions: The system should work with both internet (external) and intranet (internal-used within the company) sites.
"""

def authenticate_user(username, password, domain):
    """
    Authenticate a user with the given username and password for a specific domain.

    Args:
        username (str): The username of the user.
        password (str): The password of the user.
        domain (str): The domain the user is trying to access.

    Returns:
        bool: True if the user is authenticated, False otherwise.
    """

    # Implement your authentication logic here, for example:
    # Check if the username and password are valid
    if username == "admin" and password == "password":
        # If valid, check if the user has access to the domain
        if domain in ["example.com", "internal.com"]:
            # If the user has access, return True
            return True
    # If the username or password is invalid, or the user does not have access to the domain, return False
    return False