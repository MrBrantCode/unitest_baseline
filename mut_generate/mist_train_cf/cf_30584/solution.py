"""
QUESTION:
Implement a function `validate_redirect_url` that takes three parameters: `redirect_to` (string), `login_redirect_url` (string), and `current_host` (string), representing the URL to redirect to, the default URL to redirect to after a successful login, and the host of the current request, respectively. The function should return a safe URL for redirection. A URL is considered safe if it is within the same host as the current request or if it is a fully qualified URL. If the provided `redirect_to` URL is not safe, it should be replaced with the `login_redirect_url`.
"""

from urllib.parse import urlparse

def validate_redirect_url(redirect_to, login_redirect_url, current_host):
    def is_safe_url(url, host):
        parsed_url = urlparse(url)
        return bool(parsed_url.netloc) and parsed_url.netloc == host

    def resolve_url(url):
        if url.startswith('/'):
            return url
        else:
            return login_redirect_url

    if not is_safe_url(redirect_to, current_host):
        return resolve_url(login_redirect_url)
    else:
        return redirect_to