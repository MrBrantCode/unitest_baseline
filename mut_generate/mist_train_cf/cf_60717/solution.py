"""
QUESTION:
Write a function named `find_nones` that inspects a given tuple for None values. The function should yield the path to all None values in the form of a list of indices or keys. If a None value is found within a dictionary, the function should return the key associated with the None value. If a dictionary contains None as a key, the function should include None in the path. The function should be able to handle tuples of diverse lengths and data types, as well as any level of nesting within the tuple. If no None values are found, the function should return 'No None values found'.
"""

def find_nones(data):
    def check_for_none(val, indices=None):
        if indices is None:
            indices = []
        
        if isinstance(val, (tuple, list)):
            for idx, item in enumerate(val):
                yield from check_for_none(item, indices + [idx])
        elif isinstance(val, dict):
            for k, v in val.items():
                if k is None: 
                    yield indices + [k], 1
                if v is None: 
                    yield indices + [k], 1
                if isinstance(v, (tuple, list, dict)):
                    yield from check_for_none(v, indices+[k])
        elif val is None:
            yield indices, 1

    none_count = 0
    none_indices = []
    for indices, count in check_for_none(data):
        none_count += count
        none_indices.append(indices)
    
    if none_count == 0:
        return 'No None values found'
    else:
        return none_indices