"""
QUESTION:
Write a function `extract_domain` that takes a URL as input and returns the domain name and the top-level domain. Then, write another function `is_cctld` that takes the top-level domain as input and returns `True` if the TLD is a country code top-level domain (ccTLD), and `False` otherwise. 

The functions must only use basic string manipulation and should not use any built-in URL parsing or regular expression libraries. The list of country code top-level domains (ccTLDs) is given as ["af", "al", "dz", ...].
"""

def extract_domain(url):
    # Remove the protocol from the URL
    if "://" in url:
        url = url.split("://")[1]

    # Remove any path or query parameters from the URL
    url = url.split("/")[0]

    # Split the remaining URL by dot separators
    parts = url.split(".")

    # Extract the domain name and the top-level domain
    domain = parts[-2]
    tld = parts[-1]

    return domain, tld

def is_cctld(tld):
    # List of country code top-level domains
    cctlds = ["af", "al", "dz"]

    # Check if the TLD is in the list of ccTLDs
    return tld.lower() in cctlds