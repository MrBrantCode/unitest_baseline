"""
QUESTION:
Implement a function `validate_config(config)` that takes a dictionary as input and returns `True` if the dictionary meets the following requirements and `False` otherwise:

- The dictionary has a 'database' key with a dictionary value.
- The 'database' dictionary has a 'name' key with a non-empty string value.
- The 'database' dictionary has a 'collections' key with a dictionary value.
- The 'collections' dictionary has a 'posts' key with a dictionary value.
- The 'posts' dictionary has a 'data_relation' key with a dictionary value.
- The 'data_relation' dictionary has 'resource', 'field', and 'embeddable' keys with string, string, and boolean values respectively.

All keys and values should be present and have the correct data types as specified above.
"""

def validate_config(config):
    if not isinstance(config, dict):
        return False
    
    if 'database' not in config or not isinstance(config['database'], dict):
        return False
    
    database = config['database']
    if 'name' not in database or not isinstance(database['name'], str) or not database['name']:
        return False
    
    if 'collections' not in database or not isinstance(database['collections'], dict):
        return False
    
    collections = database['collections']
    if 'posts' not in collections or not isinstance(collections['posts'], dict):
        return False
    
    posts = collections['posts']
    if 'data_relation' not in posts or not isinstance(posts['data_relation'], dict):
        return False
    
    data_relation = posts['data_relation']
    if not all(key in data_relation for key in ['resource', 'field', 'embeddable']):
        return False
    
    if not isinstance(data_relation['resource'], str) or not isinstance(data_relation['field'], str) or not isinstance(data_relation['embeddable'], bool):
        return False
    
    return True