"""
QUESTION:
Implement the `RegexMatchFilter` subclass with a class-level `MATCH` dictionary containing key-value pairs for regular expression criteria and a `match` method that uses the `re` module to compare job attributes with the `MATCH` criteria. The `match` method should return `True` if all criteria are satisfied and `False` otherwise. The `MATCH` dictionary should contain at least two key-value pairs: one for matching job titles containing 'developer' or 'engineer' and one for matching job locations in 'New York' or 'San Francisco'.
"""

import re

def regex_match_filter(job_attributes):
    MATCH = {
        'title': r'developer|engineer',  
        'location': r'New York|San Francisco'  
    }

    result = all(re.search(v, job_attributes.get(k, '')) for k, v in MATCH.items())
    return result