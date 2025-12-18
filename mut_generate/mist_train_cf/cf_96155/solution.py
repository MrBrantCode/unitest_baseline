"""
QUESTION:
Create a function named "parse_urls" that takes a string URL as input. The function should return a dictionary of queries from the URL, handling multiple query parameters separated by "&" and nested query parameters using square brackets ("[]") in the key. If a query parameter appears multiple times in the URL, only the last occurrence should be included in the dictionary. The function should correctly parse the URL and return a dictionary where the keys are the query parameter names and the values are the corresponding query parameter values.
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