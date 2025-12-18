"""
QUESTION:
Analyze the data in a nested Python dictionary and return a dictionary with the count of each data type at each depth level. The function should handle dictionaries, lists, tuples, and basic data types. 

Function name: analyze_data

Input parameters: 
- data: a nested Python dictionary
- depth (optional): the current depth level, defaults to 0
- result (optional): a dictionary to store the results, defaults to None

Restrictions: 
- The function should be able to handle nested dictionaries with arbitrary depth
- The function should be able to handle lists and tuples as values in the dictionary
- The function should be able to handle basic data types such as integers and strings
- The function should return a dictionary with the count of each data type at each depth level
"""

from collections import defaultdict

def analyze_data(data, depth=0, result=None):
    if result is None: 
        result = defaultdict(lambda: defaultdict(int))
    
    data_type = type(data)
    result[depth][data_type.__name__] += 1

    if isinstance(data, (list, tuple)):
        for item in data:
            analyze_data(item, depth+1, result)

    elif isinstance(data, dict):
        for v in data.values():
            analyze_data(v, depth+1, result)
    
    return dict(result)