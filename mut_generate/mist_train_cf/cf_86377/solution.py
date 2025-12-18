"""
QUESTION:
Implement a function `group_and_sort` that takes in a list of dictionaries `data`, a shared key `shared_key`, another key `sorting_key`, and a specific value `remove_value`. This function should group the dictionaries in `data` by the `shared_key`, sort the groups in descending order based on the sum of the values of `shared_key`, and then by the minimum value of `sorting_key` in case of a tie. Additionally, it should remove any dictionaries from each group where the value of `sorting_key` equals `remove_value`. The function should have a time complexity of O(n log n) and a space complexity of O(n).
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