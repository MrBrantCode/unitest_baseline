"""
QUESTION:
Implement a function `validate_filters` that takes a list of filters as input, where each filter is a dictionary containing the keys 'name', 'required', and 'filters'. The function should validate the filters and return a boolean indicating whether all required filters are present. The function should handle nested filters recursively.
"""

def validate_filters(filters: list) -> bool:
    for filter in filters:
        if filter['required'] and filter['name'] not in [f['name'] for f in filter['filters']]:
            return False
        if filter['filters']:
            if not validate_filters(filter['filters']):
                return False
    return True