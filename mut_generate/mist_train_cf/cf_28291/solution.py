"""
QUESTION:
Implement a function `validate_package_metadata(metadata: dict) -> bool` that takes a dictionary `metadata` representing Python package metadata. The function should return `True` if the metadata contains all required keys with correct data types and values, and `False` otherwise.

The required keys and their corresponding data types and values are:
- 'packages': a list of strings
- 'license': a non-empty string
- 'description': a non-empty string
- 'long_description': a non-empty string
- 'long_description_content_type': the string "text/markdown"
- 'install_requires': a list of strings
- 'url': a non-empty string
- 'author': a non-empty string
- 'author_email': a non-empty string
"""

def validate_package_metadata(metadata: dict) -> bool:
    required_keys = ['packages', 'license', 'description', 'long_description', 'long_description_content_type',
                     'install_requires', 'url', 'author', 'author_email']
    
    for key in required_keys:
        if key not in metadata:
            return False
    
    if not isinstance(metadata['packages'], list) or not all(isinstance(package, str) for package in metadata['packages']):
        return False
    
    if not isinstance(metadata['license'], str) or not metadata['license']:
        return False
    
    if not isinstance(metadata['description'], str) or not metadata['description']:
        return False
    
    if not isinstance(metadata['long_description'], str) or not metadata['long_description']:
        return False
    
    if metadata['long_description_content_type'] != 'text/markdown':
        return False
    
    if not isinstance(metadata['install_requires'], list) or not all(isinstance(dep, str) for dep in metadata['install_requires']):
        return False
    
    if not isinstance(metadata['url'], str) or not metadata['url']:
        return False
    
    if not isinstance(metadata['author'], str) or not metadata['author']:
        return False
    
    if not isinstance(metadata['author_email'], str) or not metadata['author_email']:
        return False
    
    return True