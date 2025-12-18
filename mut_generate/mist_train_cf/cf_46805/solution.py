"""
QUESTION:
Write a function `flatten_json` that takes a JSON object as input, which can contain nested JSON objects and arrays, and returns a flattened dictionary representation of the JSON object. The function should use dotted notation to represent nested structures, i.e., if a key 'a' has a nested key 'b', the flattened key should be 'a_b'. The function should handle different types of JSON structures and include error checking.
"""

def flatten_json(json_object):
    out = {}
    def flatten(x, name=''):
        if type(x) is dict:
            for a in x:
                flatten(x[a], name + a + '_')
        elif type(x) is list:
            i=0
            for a in x:
                flatten(a, name + str(i) + '_')
                i += 1
        else:
            out[name[:-1]] = x
    flatten(json_object)
    return out