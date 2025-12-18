"""
QUESTION:
Write a function `consolidate_links(links)` that takes a list of URLs as input and returns a dictionary where the keys are the names of professional business networking platforms ('linkedin', 'xing', 'hubspot') and the values are lists of URLs that belong to each platform. The function should handle any number of URLs and platforms, and it should ignore malformed URLs and URLs that do not belong to any of the specified platforms. The function should also handle any exceptions that occur during URL processing.
"""

import urllib.parse

def consolidate_links(links):
    # Platforms we are interested in
    platforms = ['linkedin', 'xing', 'hubspot']
    
    # Dictionaries which will store the URLs for each platform
    url_dict = {platform: [] for platform in platforms}

    for link in links:
        try:
            # Parse the URL to get the netloc (which includes the platform in the domain)
            parsed_link = urllib.parse.urlparse(link)
            netloc = parsed_link.netloc
            
            # Check if the URL is valid (has a netloc and a scheme)
            if not (netloc and parsed_link.scheme):
                print(f"Malformed URL: {link}")
                continue
                
            # Check which platform the link belongs to
            for platform in platforms:
                if platform in netloc:
                    url_dict[platform].append(link)
                    break

        except Exception as e:
            print(f"Error processing URL: {link} Error: {str(e)}")

    return url_dict