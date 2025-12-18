"""
QUESTION:
Create a function named `process_github_urls` that takes a list of GitHub repository URLs as input and constructs the corresponding GitHub clone URLs for each repository. The function should extract the username and repository name from each URL, construct the clone URL by appending '.git' to the original URL, and return the clone URLs. The input URLs are in the format 'https://github.com/username/repo'.
"""

import re

def process_github_urls(urls):
    """
    This function takes a list of GitHub repository URLs, extracts the username and repository name, 
    constructs the corresponding GitHub clone URLs, and returns the clone URLs.
    
    Args:
        urls (list): A list of GitHub repository URLs in the format 'https://github.com/username/repo'
    
    Returns:
        list: A list of GitHub clone URLs
    """
    pattern = r'https://github.com/([^/]+)/([^/]+)$'
    clone_urls = []
    
    for url in urls:
        match = re.match(pattern, url)
        if match:
            username = match.group(1)
            repo = match.group(2)
            clone_url = f'https://github.com/{username}/{repo}.git'
            clone_urls.append(clone_url)
        else:
            clone_urls.append(None)
    
    return clone_urls