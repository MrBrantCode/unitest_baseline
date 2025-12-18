"""
QUESTION:
Write a recursive function called `get_subdomains` that takes a URL string as input and returns a list of subdomains in the correct order, even if they are nested. The function should be able to handle URLs with different protocols (like HTTPS, HTTP, FTP) and should include exception handling for invalid URLs. Do not use any prebuilt URL parsing functions.
"""

def get_subdomains(url):
    try:
        # check if the URL is valid
        if not url or url.count("://") != 1:
            raise Exception("Invalid URL")

        # splitting the URL by "://"
        protocol, url = url.split("://")

        # validate the protocol
        if protocol not in ['http', 'https', 'ftp']:
            raise Exception("Invalid protocol")

        # separate the domain and the path if exists
        url_parts = url.split("/")
        domain_path = url_parts.pop(0)

        # split the domain into subdomains
        subdomains = domain_path.split('.')

        # reverse the subdomains and return
        return subdomains[::-1]
    except Exception as e:
        print(f"Error: {e}")
        return []