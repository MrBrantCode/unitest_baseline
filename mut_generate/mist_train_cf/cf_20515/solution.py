"""
QUESTION:
Create a function named "parse_urls" that takes a string parameter representing a URL and returns a dictionary of query parameters. The URL can contain multiple query parameters separated by "&" and each query parameter can be a key-value pair separated by "=" or a nested query parameter using square brackets "[]". If a query parameter appears multiple times, only the last occurrence should be included in the dictionary. The function should handle URL-encoded values and nested query parameters correctly.
"""

def parse_urls(url):
    query_start = url.find("?")
    if query_start == -1:
        return {}
    
    query_params = url[query_start + 1:].split("&")
    result = {}
    
    for param in query_params:
        key_value = param.split("=")
        key = key_value[0]
        value = key_value[1] if len(key_value) > 1 else ""
        
        if "[" in key:
            nested_keys = key.split("[")
            nested_dict = result
            for nested_key in nested_keys[:-1]:
                if nested_key not in nested_dict:
                    nested_dict[nested_key] = {}
                nested_dict = nested_dict[nested_key]
            
            last_key = nested_keys[-1].replace("]", "")
            nested_dict[last_key] = value
        else:
            result[key] = value
    
    return result