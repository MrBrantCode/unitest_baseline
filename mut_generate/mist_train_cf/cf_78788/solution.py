"""
QUESTION:
Write a function `auth_empty_dicts` that authenticates whether a dictionary and all its embedded dictionaries, irrespective of their nesting depth, are empty. The function should concurrently calculate the aggregate count of void dictionaries and handle circular references without succumbing to an endless loop. The function should also manage other iterable entities such as lists, tuples, and sets that may be nested within the dictionaries. The function should return a tuple where the first element is a boolean value that is true exclusively if the primary dictionary and all its embedded ones are bereft of elements, and the second element is an integer symbolizing the cumulative count of void dictionaries.
"""

def auth_empty_dicts(d, track_visited=None):
    if track_visited is None:
        track_visited = set()
    else:
        if id(d) in track_visited:
            return True, 0
            
    empty_dict = {}
    count_empty = 0
    track_visited.add(id(d))
    
    if isinstance(d, dict):
        items_to_check = d.values()
        if not d:
            empty_dict = True
            count_empty += 1
        else:
            empty_dict = False
    else:
        items_to_check = d
        empty_dict = True
    
    for v in items_to_check:
        if isinstance(v, (set, list, tuple, dict)):
            v_empty, v_count = auth_empty_dicts(v, track_visited)
            empty_dict &= v_empty
            count_empty += v_count
        else:
            empty_dict = False
            
    return empty_dict, count_empty