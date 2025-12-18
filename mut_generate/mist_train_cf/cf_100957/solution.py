"""
QUESTION:
Create a Python function `classify(value)` that checks if the input `value` is `None` (null), exists in a predefined dictionary `values`, or neither. If `value` is `None`, the function should return `'Null'`. If `value` is not `None` and exists in `values`, the function should return the corresponding value from the dictionary. If `value` is not `None` and does not exist in `values`, the function should return `'Not Found'`. The function should be flexible enough to accommodate varying lookup fields by customizing the `values` dictionary.
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