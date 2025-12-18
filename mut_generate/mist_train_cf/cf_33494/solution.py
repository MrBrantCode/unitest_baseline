"""
QUESTION:
Implement the function `get_domain_names(urls)` that takes a list of URLs as input and returns a list of their corresponding domain names. The domain name is defined as the substring between the first and second occurrence of the character '/' in the URL, or the entire URL if it does not contain a second '/'.
"""

def get_domain_names(urls):
    domain_names = []
    for url in urls:
        if '/' in url[8:]:
            start_index = url.find('/') + 2
            end_index = url.find('/', start_index)
            if end_index == -1:
                domain_names.append(url[start_index:])
            else:
                domain_names.append(url[start_index:end_index])
        else:
            domain_names.append(url[8:])
    return domain_names