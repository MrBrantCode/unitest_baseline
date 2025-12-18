"""
QUESTION:
Write a function named `filter_clothes` that filters a collection based on the following conditions: the 'category' field is 'clothes', the 'color' field is 'blue', the 'size' field is either 'small' or 'medium', and the 'price' field is greater than 100.
"""

def filter_clothes(data):
    return {
        'category': 'clothes',
        'color': 'blue',
        'size': {'$in': ['small', 'medium']},
        'price': {'$gt': 100}
    }