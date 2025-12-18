"""
QUESTION:
Write a function `find_max_min` that takes a list as input, which may contain floats, strings, and nested lists. The function should return a dictionary where each key corresponds to a data type (float, str) and its corresponding value is another dictionary with "max" and "min" keys. If the input list contains nested lists, the function should recursively process them and include their results in the output dictionary.
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