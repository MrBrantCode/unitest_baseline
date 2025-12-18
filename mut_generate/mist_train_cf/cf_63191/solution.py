"""
QUESTION:
Define a function `collect_unique_values` that takes a list of dictionaries `data` and a string `field`. The function should merge dictionaries with the same 'name' field, sum their 'price' fields, and collect unique values for the specified `field`. The function should return a list of the merged dictionaries. The 'name' field is the key for merging, and the `field` argument specifies the field for which unique values should be collected.
"""

def collect_unique_values(data, field):
    result = {}
    for d in data:
        key = d['name'] # key field is 'name'
        if key not in result:
            result[key] = d
        else: # merge data with same key
            result[key]['price'] += d['price'] # add prices
            if d[field] not in result[key][field]: # collect unique values for other field
                result[key][field] += ', '+d[field]
    return list(result.values())