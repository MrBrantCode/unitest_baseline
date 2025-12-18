"""
QUESTION:
Write a function that when given a URL as a string, parses out just the domain name and returns it as a string. For example:
```python
domain_name("http://github.com/carbonfive/raygun") == "github" 
domain_name("http://www.zombie-bites.com") == "zombie-bites"
domain_name("https://www.cnet.com") == "cnet"
```
"""

def extract_domain_name(url: str) -> str:
    """
    Extracts the domain name from a given URL.

    Parameters:
    url (str): The input URL from which the domain name needs to be extracted.

    Returns:
    str: The extracted domain name.
    """
    return url.split('//')[-1].split('www.')[-1].split('.')[0]