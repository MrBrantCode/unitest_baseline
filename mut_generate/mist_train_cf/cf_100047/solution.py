"""
QUESTION:
Implement a function `find_max_min(data)` that takes a list `data` containing floats, strings, and/or nested lists as input and returns a dictionary with "max" and "min" keys for each data type found in the list. The function should recursively handle nested lists and return a nested dictionary with the same keys.
"""

def find_max_min(data):
    results = {}
    if isinstance(data, list):
        for item in data:
            if isinstance(item, float):
                if 'float' not in results:
                    results['float'] = {'max': item, 'min': item}
                else:
                    if item > results['float']['max']:
                        results['float']['max'] = item
                    if item < results['float']['min']:
                        results['float']['min'] = item
            elif isinstance(item, str):
                if 'str' not in results:
                    results['str'] = {'max': item, 'min': item}
                else:
                    if item > results['str']['max']:
                        results['str']['max'] = item
                    if item < results['str']['min']:
                        results['str']['min'] = item
            elif isinstance(item, list):
                nested_results = find_max_min(item)
                for key in nested_results:
                    if key not in results:
                        results[key] = nested_results[key]
                    else:
                        if nested_results[key]['max'] > results[key]['max']:
                            results[key]['max'] = nested_results[key]['max']
                        if nested_results[key]['min'] < results[key]['min']:
                            results[key]['min'] = nested_results[key]['min']
    return results