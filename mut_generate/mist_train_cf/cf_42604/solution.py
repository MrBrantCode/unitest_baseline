"""
QUESTION:
Update a quota set by removing specific items from its properties and required fields. Implement a function `update_quota_set` that takes a nested dictionary `original_quota_set` representing the quota set and a list `remove_item_list` of items to be removed, and returns the updated quota set with the specified items removed from the properties and required fields. The quota set's properties and required fields are nested under the keys 'response_body' > 'properties' > 'quota_set' > 'properties' and 'response_body' > 'properties' > 'quota_set' > 'required' respectively.
"""

import copy

def update_quota_set(original_quota_set: dict, remove_item_list: list) -> dict:
    update_quota_set = copy.deepcopy(original_quota_set)
    quota_properties = update_quota_set['response_body']['properties']['quota_set']['properties']
    quota_required = update_quota_set['response_body']['properties']['quota_set']['required']

    for item in remove_item_list:
        quota_properties.pop(item, None)
        if item in quota_required:
            quota_required.remove(item)

    return update_quota_set