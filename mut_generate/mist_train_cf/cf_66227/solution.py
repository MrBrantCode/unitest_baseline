"""
QUESTION:
Write a function named `parse_url` that takes a string representing a URL as input and returns a tuple containing a boolean indicating whether the URL is valid according to RFC 1738 and RFC 3986 standards, and a dictionary containing the host and path information if the URL is valid. The function should not use built-in URL parser libraries or regular expressions for URL validation.
"""

def parse_url(url):
    """
    This function takes a string representing a URL as input, 
    and returns a tuple containing a boolean indicating whether 
    the URL is valid according to RFC 1738 and RFC 3986 standards, 
    and a dictionary containing the host and path information if the URL is valid.

    :param url: A string representing a URL.
    :return: A tuple containing a boolean indicating whether the URL is valid 
             and a dictionary containing the host and path information if the URL is valid.
    """
    
    # Initialize an empty dictionary to store the host and path information
    url_info = {}
    
    # Initialize a flag to indicate whether the URL is valid
    is_valid = False
    
    # Check if the URL starts with a scheme
    if url.startswith(("http://", "https://", "ftp://")):
        # Split the URL into scheme and the rest of the URL
        scheme, rest = url.split("://", 1)
        
        # Check if the rest of the URL contains a host and a path
        if "/" in rest:
            # Split the rest of the URL into host and path
            host, path = rest.split("/", 1)
            
            # Store the host and path information in the dictionary
            url_info["host"] = host
            url_info["path"] = "/" + path
            
            # Set the flag to indicate that the URL is valid
            is_valid = True
        else:
            # If the rest of the URL does not contain a path, set the host to the rest of the URL
            url_info["host"] = rest
            url_info["path"] = ""
            
            # Set the flag to indicate that the URL is valid
            is_valid = True
    
    # Return a tuple containing the flag and the dictionary
    return is_valid, url_info