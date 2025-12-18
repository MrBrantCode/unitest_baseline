"""
QUESTION:
Write a function `group_and_sort` that takes a list of dictionaries `data`, a shared key `shared_key`, another key `sorting_key`, and a specific value `remove_value`. Group the dictionaries in `data` by `shared_key` and sort the groups in descending order based on the sum of the values of `shared_key`. If two groups have the same sum, sort them based on the minimum value of `sorting_key`. For each group, remove any dictionaries where the value of `sorting_key` equals `remove_value`. The solution should achieve a time complexity of O(n log n) and a space complexity of O(n).
"""

def group_and_sort(data, shared_key, sorting_key, remove_value):
    groups = {}
    
    for d in data:
        if d[shared_key] not in groups:
            groups[d[shared_key]] = []
        groups[d[shared_key]].append(d)
    
    groups = dict(sorted(groups.items(), key=lambda x: (-sum(d[shared_key] for d in x[1]), min(d[sorting_key] for d in x[1]))))
    
    filtered_groups = {}
    for key, value in groups.items():
        filtered_groups[key] = [d for d in value if d[sorting_key] != remove_value]
    
    return filtered_groups