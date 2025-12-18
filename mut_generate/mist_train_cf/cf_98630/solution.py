"""
QUESTION:
Create a function `classify` that takes a single argument `value`. The function should check if `value` is null, and if so, return the string `'Null'`. Otherwise, it should check if `value` exists in a predefined dictionary `values`, and if it does, return the corresponding value from the dictionary. If `value` is not null and does not exist in the `values` dictionary, the function should return the string `'Not Found'`.
"""

def classify(value):
    values = {
        'apple': 'fruit',
        'orange': 'fruit',
        'carrot': 'vegetable',
        'broccoli': 'vegetable'
    }
    if value is None:
        return 'Null'
    elif value in values:
        return values[value]
    else:
        return 'Not Found'