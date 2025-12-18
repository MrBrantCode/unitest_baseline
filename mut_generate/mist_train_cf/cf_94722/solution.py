"""
QUESTION:
Implement a function `get_names` that takes a JSON object containing a list of individuals with their names and ages. The function should return the names of all individuals whose age is greater than 25. The function should have a time complexity of O(n), where n is the number of individuals in the data.
"""

def get_names(data):
    names = []
    
    for item in data['data']:
        if item['age'] > 25:
            names.append(item['name'])
    
    return names