"""
QUESTION:
Create a function named `parse_query_string` that takes a URL string as input and returns a dictionary of key-value pairs from the URL query string. If a key is repeated in the query string, only the last occurrence should be stored in the dictionary. The URL may contain special characters such as percent-encoded values.
"""

def parse_query_string(url):
    # Find the query string in the URL
    query_start_index = url.find('?')
    if query_start_index == -1:
        return {}
    
    query_string = url[query_start_index+1:]
    
    # Split the query string into individual key-value pairs
    pairs = query_string.split('&')
    
    # Create an empty dictionary to store the key-value pairs
    query_dict = {}
    
    # Process each key-value pair
    for pair in pairs:
        # Split the pair into the key and the value
        key, value = pair.split('=')
        
        # Decode percent-encoded values
        value = value.replace('%20', ' ')
        
        # Store the key-value pair in the dictionary
        query_dict[key] = value
    
    return query_dict