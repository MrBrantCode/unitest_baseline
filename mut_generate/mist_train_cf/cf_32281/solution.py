"""
QUESTION:
Create a function `extractDomainName(url: string): string` that takes a URL as input and returns the domain name. The input URL starts with either "http://" or "https://" and contains at least one "/". The domain name is the sequence of characters between the "http://" or "https://" and the next "/".
"""

def extractDomainName(url: str) -> str:
    start_index = url.find("//") + 2
    end_index = url.find("/", start_index)
    return url[start_index:end_index]