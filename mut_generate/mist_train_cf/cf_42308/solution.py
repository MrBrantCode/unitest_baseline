"""
QUESTION:
Implement a function `custom_sort(objects, options)` that takes a list of dictionaries `objects` and a dictionary `options` as input. The `options` dictionary must contain a key `'ordering'` with a list of attribute names as its value. The function should return the list of objects sorted in ascending order based on the specified attributes in the order of priority.
"""

def custom_sort(objects, options):
    ordering = options.get('ordering', [])
    
    def custom_key(obj):
        return tuple(obj[attr] for attr in ordering)
    
    return sorted(objects, key=custom_key)