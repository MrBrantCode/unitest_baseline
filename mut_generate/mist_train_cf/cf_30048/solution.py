"""
QUESTION:
Implement the `computeContribs` function to calculate the contributions of outbound links from a page to the rank of other pages. The function takes two parameters: `urls` (a non-empty list of URLs representing outbound links from a page) and `rank` (a non-negative float representing the current rank of the page). The function should return a list of tuples, where each tuple contains the URL of an outbound link and its contribution to the rank of other pages, calculated by dividing the rank of the page by the total number of outbound links.
"""

def computeContribs(urls, rank):
    num_urls = len(urls)
    if num_urls == 0:
        return []
    contrib = rank / num_urls
    return [(url, contrib) for url in urls]