"""
QUESTION:
Implement a function `get_names(data)` that takes a JSON object `data` containing a list of individuals with their names and ages, and returns a list of names of individuals whose age is greater than 25. The function should have a time complexity of O(n), where n is the number of individuals in the data.
"""

def get_names(data):
    return [item['name'] for item in data['data'] if item['age'] > 25]