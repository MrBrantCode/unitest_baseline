"""
QUESTION:
Create a function named `sort_dict_list` that takes a list of dictionaries as input, filters out dictionaries that do not have a key "status" with the value "active", and returns the filtered list sorted in ascending order of "count". If multiple dictionaries have the same "count" value, they should be sorted in descending order of the length of their "name" value. The sorting should be stable, preserving the relative order of dictionaries with the same "count" and "name" length.
"""

def sort_dict_list(lst):
    active_dicts = [d for d in lst if d.get("status") == "active"]
    sorted_dicts = sorted(active_dicts, key=lambda x: (x["count"], -len(x["name"])), reverse=False)
    return sorted_dicts