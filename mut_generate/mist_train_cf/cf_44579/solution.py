"""
QUESTION:
Implement a function `mergeLists(keys, values)` that merges two lists into a dictionary. The `keys` list serves as the dictionary keys, and the `values` list serves as the dictionary values. 

If the lists are of different lengths, fill in the missing keys/values with `None`. If the `values` list contains duplicate entries for a given key, maintain a count of those duplicates in the resultant dictionary. 

The function should handle empty input lists and avoid using mutable data types (e.g., lists, dictionaries) as dictionary keys.
"""

def mergeLists(keys, values):
    # lengths of input lists
    len_keys, len_values = len(keys), len(values)
    
    res = {}
  
    # Fill in None for missing keys/values
    if len_keys > len_values:
        for i in range(len_keys - len_values):
            values.append(None)
    elif len_keys < len_values:
        for i in range(len_values - len_keys):
            keys.append(None)
      
    # Merge values and counts
    for i in range(len(keys)):
        if isinstance(keys[i], list) or isinstance(keys[i], dict):
            continue
        
        if keys[i] in res:
            if values[i] not in res[keys[i]]:
                res[keys[i]][values[i]] = 1
            else:
                res[keys[i]][values[i]] += 1
        else:
            res[keys[i]] = {values[i]: 1}
      
    return res